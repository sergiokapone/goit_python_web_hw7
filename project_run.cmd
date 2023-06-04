@echo off

:menu
REM Меню вибору дії
cls
echo 1. Restart Docker
echo 2. Generate data
echo 3. Generate queries
echo 4. Start CRUD console application 
echo 5. Exit
echo.

set /p CHOICE=">>> "

if %CHOICE%==1 goto docker
if %CHOICE%==2 goto generate
if %CHOICE%==3 goto queries
if %CHOICE%==4 goto crud
if %CHOICE%==5 exit

:docker
call docker_run.cmd
pause
goto menu

:generate
pipenv run python seed.py
pause
goto menu

:queries
pipenv run python my_select.py
pause
goto menu

:crud
pipenv run python main.py
set /p OPTIONS="Type CLI options: "
pipenv run python main.py %OPTIONS%
pause
goto menu