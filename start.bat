@echo off
REM Quick startup script for Student CRUD System
REM This script starts the Django development server

echo.
echo ====================================
echo  Student CRUD System - Quick Start
echo ====================================
echo.

cd crud_project

echo Checking Django setup...
py manage.py check

if errorlevel 1 (
    echo.
    echo Error: Django setup check failed!
    echo Please ensure all dependencies are installed.
    pause
    exit /b 1
)

echo.
echo.
echo ✅ Starting development server...
echo.
echo 📚 Student CRUD System is running!
echo.
echo 🌐 Access the application at:
echo    - Students: http://localhost:8000/students/
echo    - Admin Panel: http://localhost:8000/admin/
echo.
echo 📖 Reference Guide: See CRUD_REFERENCE.md
echo.
echo Press CTRL+C to stop the server
echo.

py manage.py runserver

pause
