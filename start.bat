@echo off

if exist .venv\NUL goto start 

:: create venv
python -m venv .venv

:: source venv
call .\.venv\Scripts\activate.bat

:: install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

:start

:: source venv
call .\.venv\Scripts\activate.bat

:: upgrade db
flask --app src\app.py db upgrade

:: run app
flask --app src\app.py run --debug --extra-files assets/ 