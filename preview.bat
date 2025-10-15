@echo off
echo 🚀 Starting preview server...
echo ================================================

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python or use npm preview instead.
    echo 📦 Try: npm run preview-alt
    pause
    exit /b 1
)

REM Start the preview server
echo 📱 Opening http://localhost:3000 in your browser...
echo ⏹️  Press Ctrl+C to stop the server
echo.

python preview.py

pause
