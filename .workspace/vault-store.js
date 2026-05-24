/* ============================================================
   vault-store.js - IndexedDB persistence for vault FileSystemDirectoryHandle.

   Why this file exists:
   - The File System Access API gives us a live FileSystemDirectoryHandle.
   - Chrome (since v86) lets us write that handle into IndexedDB
     (structured-clone preserves it). On the next visit we can pull it back
     out and call queryPermission() to see whether the user has to re-grant
     access. If permission is still 'granted', the artefact auto-reconnects.
   - This is the standard pattern documented at
     https://developer.chrome.com/articles/file-system-access/#stored-file-or-directory-handles-and-permissions

   Public surface (attached to window.vaultStore):
     openDB()                 -> Promise<IDBDatabase>
     saveHandle(handle)       -> Promise<void>
     loadHandle()             -> Promise<FileSystemDirectoryHandle|null>
     clearHandle()            -> Promise<void>
     verifyPermission(handle) -> Promise<'granted'|'prompt'|'denied'>
     requestPermission(handle)-> Promise<'granted'|'prompt'|'denied'>

   No external dependencies. Loaded as a plain script before the artefact
   inline script (see graph.html and positions.html).
   ============================================================ */

(function () {
  const DB_NAME = 'wiki-tokenise';
  const DB_VERSION = 1;
  const STORE = 'handles';
  const KEY = 'vault';

  function openDB() {
    return new Promise((resolve, reject) => {
      const req = indexedDB.open(DB_NAME, DB_VERSION);
      req.onupgradeneeded = () => {
        const db = req.result;
        if (!db.objectStoreNames.contains(STORE)) {
          db.createObjectStore(STORE);
        }
      };
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
  }

  function withStore(mode, fn) {
    return openDB().then(db => new Promise((resolve, reject) => {
      const tx = db.transaction(STORE, mode);
      const store = tx.objectStore(STORE);
      const result = fn(store);
      tx.oncomplete = () => resolve(result);
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    }));
  }

  function saveHandle(handle) {
    return withStore('readwrite', store => store.put(handle, KEY));
  }

  function loadHandle() {
    return new Promise((resolve, reject) => {
      openDB().then(db => {
        const tx = db.transaction(STORE, 'readonly');
        const req = tx.objectStore(STORE).get(KEY);
        req.onsuccess = () => resolve(req.result || null);
        req.onerror = () => reject(req.error);
      }).catch(reject);
    });
  }

  function clearHandle() {
    return withStore('readwrite', store => store.delete(KEY));
  }

  // Returns one of: 'granted' | 'prompt' | 'denied'.
  // Read-only by default (matches showDirectoryPicker({ mode: 'read' })).
  async function verifyPermission(handle, writable = false) {
    if (!handle) return 'denied';
    const opts = { mode: writable ? 'readwrite' : 'read' };
    try {
      return await handle.queryPermission(opts);
    } catch (err) {
      return 'denied';
    }
  }

  // Must be called from within a user gesture (click handler). Browsers
  // refuse the prompt otherwise.
  async function requestPermission(handle, writable = false) {
    if (!handle) return 'denied';
    const opts = { mode: writable ? 'readwrite' : 'read' };
    try {
      const current = await handle.queryPermission(opts);
      if (current === 'granted') return 'granted';
      return await handle.requestPermission(opts);
    } catch (err) {
      return 'denied';
    }
  }

  window.vaultStore = {
    openDB,
    saveHandle,
    loadHandle,
    clearHandle,
    verifyPermission,
    requestPermission,
  };
})();
