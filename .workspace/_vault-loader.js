/* ============================================================
   _vault-loader.js — shared vault walker + frontmatter parser.
   Reads every markdown file under a FileSystemDirectoryHandle,
   parses YAML frontmatter (minimal subset), resolves wikilinks.
   No third-party deps (uses native showDirectoryPicker + a
   hand-written frontmatter parser).

   Public surface:
     window.vaultLoader = {
       connect()        -> Promise<{handle, notes}>
       reconnect()      -> Promise<{handle, notes} | null>
       forget()         -> Promise<void>
       walkAll(handle)  -> Promise<Note[]>
       parseFrontmatter(text) -> {fm, body}
       resolveLink(s)   -> 'slug'  (strip [[ ]] and pipe aliases)
     }
   Note = {
     path, name, slug,
     fm,        // parsed frontmatter object
     body,      // markdown body text
     links,     // [target-slug, ...]
   }
   ============================================================ */
(function () {
  const store = window.vaultStore;

  function apiAvailable() {
    return typeof window !== 'undefined' && 'showDirectoryPicker' in window;
  }

  async function connect() {
    if (!apiAvailable()) {
      throw new Error(
        'This page must be opened in Chrome 86+ or Edge 86+ on http://localhost (not file:// or a sandboxed preview). ' +
        'From .workspace/, run serve.bat (Windows) or ./serve.sh, then open http://localhost:8766/index.html.'
      );
    }
    const handle = await window.showDirectoryPicker({ mode: 'read' });
    await store.saveHandle(handle);
    console.log('[wiki-tokenise] vault connected; walking files...');
    const notes = await walkAll(handle);
    console.log(`[wiki-tokenise] loaded ${notes.length} notes from vault.`);
    return { handle, notes };
  }

  async function reconnect() {
    const handle = await store.loadHandle();
    if (!handle) return null;
    let perm = await store.verifyPermission(handle);
    if (perm !== 'granted') {
      // Best-effort silent re-request. Chrome sometimes accepts the
      // page-navigation gesture as still active; if not, this returns
      // 'denied' inside the try/catch and we fall through.
      perm = await store.requestPermission(handle);
    }
    if (perm === 'granted') {
      const notes = await walkAll(handle);
      return { handle, notes };
    }
    return { handle, notes: null, needsPermission: true };
  }

  async function requestAfterGesture(handle) {
    const perm = await store.requestPermission(handle);
    if (perm !== 'granted') return null;
    return walkAll(handle);
  }

  // Convenience: when an artefact's init detects needsPermission, call
  // this to attach a one-shot click-anywhere handler that re-requests
  // permission on the first user gesture. Calls `onReady(notes)` once
  // the vault loads.
  function autoReconnectOnClick(handle, onReady) {
    const once = async (ev) => {
      // Ignore clicks on links - let nav happen normally.
      if (ev.target && ev.target.closest && ev.target.closest('a[href]')) return;
      document.removeEventListener('click', once, true);
      const notes = await requestAfterGesture(handle);
      if (notes) onReady(notes);
    };
    document.addEventListener('click', once, true);
  }

  async function forget() {
    await store.clearHandle();
  }

  async function walkAll(handle) {
    const notes = [];
    await walkDir(handle, '', notes, 0);
    // Resolve wikilinks per note.
    for (const n of notes) {
      n.links = extractLinks(n.body);
    }
    return notes;
  }

  async function walkDir(dir, prefix, out, depth) {
    if (depth > 12) return;
    for await (const entry of dir.values()) {
      // Skip hidden + binary-heavy folders.
      if (entry.name.startsWith('.')) continue;
      if (entry.name === 'node_modules' || entry.name === '.git') continue;
      if (entry.name === '80_Attachments') continue;
      const rel = prefix ? prefix + '/' + entry.name : entry.name;
      if (entry.kind === 'directory') {
        await walkDir(entry, rel, out, depth + 1);
      } else if (entry.kind === 'file' && entry.name.endsWith('.md')) {
        try {
          const f = await entry.getFile();
          const text = await f.text();
          const { fm, body } = parseFrontmatter(text);
          const baseName = entry.name.replace(/\.md$/, '');
          out.push({
            path: rel,
            name: baseName,
            slug: baseName,
            fm,
            body,
            links: [],
          });
        } catch (e) {
          console.warn('skip', rel, e);
        }
      }
    }
  }

  // Minimal YAML frontmatter parser. Handles scalar strings, numbers,
  // booleans, flow-style lists, and one-line key: value pairs. Sufficient
  // for the controlled vocabulary in 99_Meta/schema.md.
  function parseFrontmatter(text) {
    const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
    if (!m) return { fm: {}, body: text };
    const fm = {};
    const lines = m[1].split(/\r?\n/);
    let curKey = null;
    for (let raw of lines) {
      if (!raw.trim()) continue;
      if (raw.startsWith('  - ')) {
        if (curKey && !Array.isArray(fm[curKey])) fm[curKey] = [];
        if (curKey) fm[curKey].push(parseScalar(raw.slice(4).trim()));
        continue;
      }
      const kv = raw.match(/^([A-Za-z_][\w\-]*):\s*(.*)$/);
      if (!kv) continue;
      const key = kv[1];
      let val = kv[2];
      if (val === '') {
        fm[key] = null;
        curKey = key;
        continue;
      }
      // Flow-style list: [a, b, c]
      const flowList = val.match(/^\[(.*)\]$/);
      if (flowList) {
        const inner = flowList[1].trim();
        fm[key] = inner === ''
          ? []
          : inner.split(',').map(s => parseScalar(s.trim()));
        curKey = null;
        continue;
      }
      fm[key] = parseScalar(val);
      curKey = key;
    }
    return { fm, body: m[2] };
  }

  function parseScalar(s) {
    if (s === '') return null;
    if (s === 'true') return true;
    if (s === 'false') return false;
    if (s === 'null' || s === '~') return null;
    if (/^-?\d+$/.test(s)) return parseInt(s, 10);
    if (/^-?\d*\.\d+$/.test(s)) return parseFloat(s);
    if ((s.startsWith('"') && s.endsWith('"')) ||
        (s.startsWith("'") && s.endsWith("'"))) {
      return s.slice(1, -1);
    }
    return s;
  }

  function extractLinks(body) {
    const out = new Set();
    const re = /\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g;
    let m;
    while ((m = re.exec(body)) !== null) {
      out.add(resolveLink(m[1]));
    }
    return Array.from(out);
  }

  function resolveLink(s) {
    // Strip path prefix and #anchor; return final slug.
    s = s.split('#')[0];
    const parts = s.split('/').filter(Boolean);
    let last = parts[parts.length - 1] || '';
    last = last.replace(/\.md$/, '');
    return last.trim();
  }

  window.vaultLoader = {
    apiAvailable,
    connect,
    reconnect,
    requestAfterGesture,
    autoReconnectOnClick,
    forget,
    walkAll,
    parseFrontmatter,
    extractLinks,
    resolveLink,
  };

  // Auto-banner: if the page is not served from http://localhost (file:// or a
  // sandboxed preview frame), or if showDirectoryPicker is missing entirely,
  // surface a clear instruction at the top of the body.
  function showEnvBanner() {
    const isLocal = /^https?:\/\/(localhost|127\.0\.0\.1)/i.test(location.href);
    const hasApi = apiAvailable();
    if (isLocal && hasApi) return;
    const banner = document.createElement('div');
    banner.style.cssText = [
      'position:sticky', 'top:0', 'z-index:99',
      'background:oklch(94% 0.030 25)', 'color:oklch(20% 0.010 260)',
      'border-bottom:1px solid oklch(38% 0.120 25)',
      "font-family:'iA Writer Quattro V', system-ui, sans-serif",
      'font-size:14px', 'line-height:1.5',
      'padding:14px 24px',
    ].join(';');
    banner.innerHTML = hasApi
      ? '<b>Open this page via the local server</b> &mdash; Chrome blocks vault access from file:// and sandboxed previews. From <code>.workspace/</code> run <code>serve.bat</code> (or <code>./serve.sh</code>), then open <a href="http://localhost:8766/index.html" style="color:inherit;">http://localhost:8766/index.html</a> in Chrome 86+ or Edge 86+.'
      : '<b>Browser does not support the File System Access API.</b> Open this page in Chrome 86+ or Edge 86+, served from http://localhost. From <code>.workspace/</code> run <code>serve.bat</code> (or <code>./serve.sh</code>), then visit <a href="http://localhost:8766/index.html" style="color:inherit;">http://localhost:8766/index.html</a>.';
    // Insert after <header> if present, else at the top of body.
    document.addEventListener('DOMContentLoaded', () => {
      const header = document.querySelector('header.app-header');
      if (header && header.parentNode) {
        header.parentNode.insertBefore(banner, header.nextSibling);
      } else {
        document.body.insertBefore(banner, document.body.firstChild);
      }
    });
  }
  showEnvBanner();
})();
