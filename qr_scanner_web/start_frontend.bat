@echo off
cd /d "C:\Users\INDRAYUDH\sign_to_speech\qr_scanner_web"
echo.
echo Starting QR Scanner Frontend...
echo Opening http://localhost:8080 in browser...
echo Press Ctrl+C to stop
echo.
python -m http.server 8080
pause
