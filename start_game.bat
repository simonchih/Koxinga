@echo off
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" koxinga.py
) else (
    python koxinga.py
)
if errorlevel 1 pause
