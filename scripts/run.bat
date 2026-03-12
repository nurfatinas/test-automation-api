@echo off
rem -----------------------
rem Test Automation Runner
rem -----------------------

rem Set environment variable
set TEST_ENV=uat

rem Set current directory and paths
set "curr=%~dp0"
set "env_path=%curr%TA_env"
set "report_path=%curr%artifact\report.html"

rem Create artifact folder if it doesn't exist
if not exist "%curr%artifact" mkdir "%curr%artifact"

rem Create virtual environment if it doesn't exist
if not exist "%env_path%\Scripts\activate" (
    python -m venv "%env_path%"
)

rem Activate virtual environment
call "%env_path%\Scripts\activate"

rem Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r "requirements.txt"

echo ================================
echo TEST AUTOMATION STARTING
echo ================================

rem Run pytest and generate HTML report
python -m pytest -v "%curr%tests" --html="%report_path%" -m smoke

rem Open the report automatically
start "" "%report_path%"