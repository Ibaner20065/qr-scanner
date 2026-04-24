@echo off
REM Team QR Scanner - Easy Launcher Script
REM This script handles setup and launches both backend and frontend

setlocal enabledelayedexpansion

echo.
echo ========================================
echo   TEAM QR SCANNER - LAUNCHER
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if dependencies are installed
python -c "import fastapi" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies
        pause
        exit /b 1
    )
    echo [OK] Dependencies installed
    echo.
)

REM Create startup batch files
echo Creating startup scripts...

REM Backend startup script
(
    echo @echo off
    echo cd /d "%cd%"
    echo echo.
    echo echo Starting QR Scanner Backend...
    echo echo Press Ctrl+C to stop
    echo echo.
    echo python backend.py
    echo pause
) > start_backend.bat

REM Frontend startup script
(
    echo @echo off
    echo cd /d "%cd%"
    echo echo.
    echo echo Starting QR Scanner Frontend...
    echo echo Opening http://localhost:8080 in browser...
    echo echo Press Ctrl+C to stop
    echo echo.
    echo python -m http.server 8080
    echo pause
) > start_frontend.bat

REM Instructions
echo.
echo ========================================
echo SETUP COMPLETE!
echo ========================================
echo.
echo Two scripts have been created:
echo   • start_backend.bat   (Run backend)
echo   • start_frontend.bat  (Run frontend)
echo.
echo QUICK START:
echo   1. Open start_backend.bat
echo   2. Wait for "Application startup complete"
echo   3. Open start_frontend.bat
echo   4. Browser will open to http://localhost:8080
echo.
echo OR run both commands in separate terminals:
echo   Terminal 1: python backend.py
echo   Terminal 2: python -m http.server 8080
echo.
echo TO DOWNLOAD QR CODES:
echo   Click "Download QR Codes" button in web interface
echo.
echo ========================================
echo.
pause
