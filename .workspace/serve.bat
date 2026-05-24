@echo off
REM wiki-tokenise launcher (Windows).
REM Double-click from Windows File Explorer (not from a code editor sidebar).
REM A console window opens, prints a URL, and waits.
REM Click the URL (Ctrl+click in most terminals) or copy it into your browser.
REM Close the window or press Ctrl+C to stop the server.

setlocal
title wiki-tokenise server
set PORT=8766
cd /d "%~dp0"

set PY=
where python >nul 2>nul && set PY=python
if not defined PY (
  where py >nul 2>nul && set PY=py
)
if not defined PY (
  echo.
  echo ERROR: Python 3 was not found on PATH.
  echo Install from https://www.python.org/downloads/windows/
  echo Check "Add python.exe to PATH" during installation, then re-run.
  echo.
  pause
  exit /b 1
)

%PY% -u serve.py --port %PORT%

echo.
echo Server stopped (exit code %ERRORLEVEL%).
pause
endlocal
