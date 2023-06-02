@echo off
chcp 65001 > nul

set ALEMBIC_PATH=.venv\Scripts
set ALEMBIC_CONFIG=alembic.ini

:menu
REM Меню вибору дії
cls
echo 1. Сгенерировать миграцию
echo 2. Применить все миграции
echo 3. Откатить последнюю миграцию
echo 4. Просмотреть текущее состояние миграций
echo 5. Выйти

set /p CHOICE=">>> "
if %CHOICE%==1 goto generate
if %CHOICE%==2 goto upgrade
if %CHOICE%==3 goto downgrade
if %CHOICE%==4 goto current_state
if %CHOICE%==5 exit
echo.

goto menu

REM Команда для створення порожньої міграції
:generate
set /p MIGRATION_NAME="Выберите имя миграции: "
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

