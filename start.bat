@echo off

if exist .venv\windows\NUL goto start 

:: create venv
python -m venv .venv\windows

:: source venv
call .\.venv\windows\Scripts\activate.bat

:: install requirements
pip install -r requirements.txt

:start

:: source venv
call .\.venv\windows\Scripts\activate.bat

:: run app
flask --app src\app.py --debug run