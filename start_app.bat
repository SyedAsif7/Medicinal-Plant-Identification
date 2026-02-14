@echo off
REM Medicinal Plant AI Classifier - Windows Startup Script

title Medicinal Plant AI Classifier

echo ========================================
echo   Medicinal Plant AI Classifier
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "app.py" (
    echo ERROR: app.py not found
    echo Please run this script from the project directory
    pause
    exit /b 1
)

if not exist "medicinal_plant_classifier.h5" (
    echo ERROR: Model file not found
    echo Please ensure 'medicinal_plant_classifier.h5' is in the project directory
    pause
    exit /b 1
)

echo Starting the application...
echo.
echo The web interface will be available at: http://localhost:8501
echo.
echo Press CTRL+C to stop the application
echo.

streamlit run app.py

pause