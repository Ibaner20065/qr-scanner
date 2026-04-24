@echo off
REM Quick start script for QR Scanner

echo.
echo ========================================
echo   Team QR Scanner - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Dependencies installed successfully!
echo ========================================
echo.
echo.
echo Next steps:
echo 1. In this terminal: python backend.py
echo 2. In another terminal: python -m http.server 8080
echo 3. Open browser and go to: http://localhost:8080
echo.
pause
