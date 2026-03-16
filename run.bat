@echo off

echo ===============================
echo Running API Automation Tests
echo ===============================

REM activate virtual environment if exists
IF EXIST venv\Scripts\activate (
    call venv\Scripts\activate
)

REM create reports folder if not exists
IF NOT EXIST reports (
    mkdir reports
)

REM run pytest
pytest -v --html=reports\report.html --self-contained-html
@REM pytest -n 4 -v --html=reports\report.html --self-contained-html

echo ===============================
echo Test Execution Completed
echo ===============================

pause