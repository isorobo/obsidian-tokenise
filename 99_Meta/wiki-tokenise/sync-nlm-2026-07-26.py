"""Push unsynced sources to the tokenise NotebookLM notebook.

Implements the /wiki-tokenise notebooklm-sync subcommand. Walks
10_Sources/ for notes whose frontmatter carries an empty nlm_id,
pushes the canonical_url (preferred) or local_attachment via the
notebooklm CLI, and writes the returned source_id back into the
note's frontmatter.

Usage:
    python 99_Meta/wiki-tokenise/sync-nlm-2026-07-26.py --dry-run
    python 99_Meta/wiki-tokenise/sync-nlm-2026-07-26.py
"""

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SOURCES = VAULT / "10_Sources"
NOTEBOOK = "d9fa07bb-4802-4626-8855-ba899655ab2b"
LOG_DIR = VAULT / "99_Meta" / "wiki-tokenise" / "state" / "logs"

EMPTY_NLM = re.compile(r'^nlm_id:\s*(?:""|\'\')?\s*$')
FIELD = re.compile(r'^([A-Za-z_]+):\s*(.*?)\s*$')


def frontmatter_lines(text):
    """Return (start, end) line indices of the frontmatter block, or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, lines
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return (0, i), lines
    return None, lines


def parse_note(path):
    """Return (needs_sync, url, nlm_line_idx, lines) for one source note."""
    text = path.read_text(encoding="utf-8")
    span, lines = frontmatter_lines(text)
    if span is None:
        return False, None, None, lines
    url = None
    nlm_idx = None
    for i in range(span[0] + 1, span[1]):
        if EMPTY_NLM.match(lines[i]):
            nlm_idx = i
            continue
        m = FIELD.match(lines[i])
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip('"').strip("'").strip()
        if key == "nlm_skip" and value == "true":
            return False, None, None, lines
        if key == "url" and value:
            url = value
    if nlm_idx is None:
        return False, None, None, lines
    if url and not url.startswith(("http://", "https://")):
        url = None
    return True, url, nlm_idx, lines


def push(target):
    """Add one source to the notebook. Returns (source_id, error)."""
    cmd = [
        "notebooklm", "source", "add", target,
        "--notebook", NOTEBOOK, "--json",
    ]
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=300, shell=False,
        )
    except subprocess.TimeoutExpired:
        return None, "timeout after 300s"
    out = result.stdout.strip()
    try:
        payload = json.loads(out[out.index("{"):])
    except (ValueError, json.JSONDecodeError):
        return None, (result.stderr.strip() or out or "no output")[:300]
    if payload.get("error"):
        return None, payload.get("message", "unknown error")[:300]
    source_id = payload.get("source_id")
    if not source_id:
        return None, f"no source_id in response: {out[:200]}"
    return source_id, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    notes = sorted(SOURCES.rglob("*.md"))
    pending, skipped = [], []
    for path in notes:
        needs, target, nlm_idx, lines = parse_note(path)
        if not needs:
            continue
        if target is None:
            skipped.append(path)
            continue
        pending.append((path, target, nlm_idx, lines))

    print(f"pending: {len(pending)}  skipped (no url/attachment): {len(skipped)}")
    for path in skipped:
        print(f"  SKIP {path.relative_to(VAULT)}")

    if args.dry_run:
        for path, target, _, _ in pending:
            print(f"  PUSH {path.relative_to(VAULT)} -> {target}")
        return 0

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    log_path = LOG_DIR / f"nlm-sync-{stamp}.log"
    added = failed = 0
    with log_path.open("w", encoding="utf-8") as log:
        for n, (path, target, nlm_idx, lines) in enumerate(pending, 1):
            if args.limit and added >= args.limit:
                break
            rel = path.relative_to(VAULT)
            source_id, error = push(target)
            if error:
                failed += 1
                print(f"[{n}/{len(pending)}] FAIL {rel}: {error}")
                log.write(f"FAIL\t{rel}\t{error}\n")
                if "Authentication" in error:
                    print("Authentication lost. Stopping. Run: notebooklm login")
                    break
                continue
            lines[nlm_idx] = f'nlm_id: "{source_id}"'
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            added += 1
            print(f"[{n}/{len(pending)}] OK   {rel} -> {source_id}")
            log.write(f"OK\t{rel}\t{source_id}\n")
            time.sleep(2)
        log.write(f"SUMMARY\tadded={added}\tfailed={failed}\tskipped={len(skipped)}\n")

    print(f"done: added={added} failed={failed} skipped={len(skipped)}")
    print(f"log: {log_path.relative_to(VAULT)}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
