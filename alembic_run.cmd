@echo off
::chcp 65001 > nul

set ALEMBIC_PATH=.venv\Scripts
set ALEMBIC_CONFIG=alembic.ini

:menu
REM Меню вибору дії
cls
echo 1. Generate a migration
echo 2. Apply all migrations
echo 3. Rollback the last migration
echo 4. View the current migration status
echo 5. Exit
echo.

set /p CHOICE=">>> "
if %CHOICE%==1 goto generate
if %CHOICE%==2 goto upgrade
if %CHOICE%==3 goto downgrade
if %CHOICE%==4 goto current_state
if %CHOICE%==5 exit


goto menu

REM Команда для створення порожньої міграції
:generate
set /p MIGRATION_NAME="Select a migration name: "
%ALEMBIC_PATH%\alembic.exe -c %ALEMBIC_CONFIG% revision --autogenerate -m "%MIGRATION_NAME%"
pause
goto menu

REM Команда для застосування всіх міграцій
:upgrade
%ALEMBIC_PATH%\alembic.exe -c %ALEMBIC_CONFIG% upgrade head
pause
goto menu

REM Команда для відкату останньої міграції
:downgrade
%ALEMBIC_PATH%\alembic.exe -c %ALEMBIC_CONFIG% downgrade -1
pause
goto menu

REM Команда для перегляду поточного стану міграцій
:current_state
%ALEMBIC_PATH%\alembic.exe -c %ALEMBIC_CONFIG% current
pause
goto menu

