
@echo off

cd /d "%~dp0"

call venv\Scripts\activate.bat

echo Starting MIS Data Cleaning...
python python\data_cleaning.py

if errorlevel 1 exit /b 1

echo Running Data Validation...
python python\data_validation.py

if errorlevel 1 exit /b 1

echo Generating MIS Reports...
python python\generate_reports.py

if errorlevel 1 exit /b 1

echo.
echo MIS Reporting Completed Successfully!

pause
