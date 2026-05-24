#!/usr/bin/env python3
"""Cross-platform launcher for the wiki-tokenise browser artefacts.

Starts a local HTTP server in this folder and prints a clickable URL.
The user clicks the URL (modern terminals make http:// links clickable)
or copies it into their browser. Runs until interrupted with Ctrl+C.

Why no auto-open: every Windows browser-launch path tried (webbrowser,
os.startfile, subprocess Popen with cmd /c start) either blocked the
HTTP serve loop in certain console-handle configurations or surfaced
the cryptic "Windows cannot find '\\\\'" dialog from `start`'s arg
parser. Printing the URL is the reliable cross-platform fallback.

Why a local server is needed: Chrome refuses to load ES module imports
and the File System Access permission flow from file:// URLs because
each file is treated as a unique opaque origin. http://localhost is a
single secure context, so all of that works.

Usage:
    python serve.py              # default port 8766
    python serve.py --port 5500  # pick a different port

Standard library only. No third-party dependencies.
"""
import argparse
import http.server
import os
import socketserver
import sys
from pathlib import Path

DEFAULT_PORT = 8766
DEFAULT_PAGE = 'index.html'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--port', type=int, default=DEFAULT_PORT,
                        help=f'port to listen on (default {DEFAULT_PORT})')
    parser.add_argument('--page', default=DEFAULT_PAGE,
                        help=f'page to open (default {DEFAULT_PAGE})')
    args = parser.parse_args()

    # Serve from the directory this script lives in, not the caller's CWD.
    os.chdir(Path(__file__).resolve().parent)

    class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
        # Prevent browser caching during development so edits to HTML / CSS /
        # JS are picked up by a normal reload (no need for Ctrl+Shift+R).
        def end_headers(self):
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()

    handler = NoCacheHandler
    # Allow port reuse so a quick restart does not hit "address in use".
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(('127.0.0.1', args.port), handler) as httpd:
            url = f'http://localhost:{args.port}/{args.page}'
            print('', flush=True)
            print('  ==========================================================', flush=True)
            print('  wiki-vault server is running.', flush=True)
            print('', flush=True)
            print(f'  Open this URL in Chrome or Edge:', flush=True)
            print('', flush=True)
            print(f'      {url}', flush=True)
            print('', flush=True)
            print('  (Most terminals make the URL above clickable - try', flush=True)
            print('   Ctrl+click. Or copy and paste into your browser.)', flush=True)
            print('', flush=True)
            print('  Keep this window open. Close it or press Ctrl+C to stop.', flush=True)
            print('  ==========================================================', flush=True)
            print('', flush=True)
            httpd.serve_forever()
    except OSError as err:
        print(f'Failed to bind port {args.port}: {err}', file=sys.stderr)
        print('Try a different port with --port 5500 (8000, 3000, 8080 also work).',
              file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print('\nStopped.')
        return 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
