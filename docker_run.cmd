REM Run if Docker is installed on the system
@echo off
REM Перевіряємо наявність контейнера
docker ps -a -f name=students | findstr students
IF %ERRORLEVEL% EQU 0 (
    docker rm --force students
    echo Container "students" was deleted.
) ELSE (
    echo Container "students" not found.
)

SET "CURRENT_PATH=%~dp0"

:: Для збереження бази на хостововій машиші
::docker volume create students_data
::docker run --name students -p 5432:5432 -e POSTGRES_PASSWORD=password -v %CURRENT_PATH%/db:/var/lib/postgresql/data -d postgres

::Для збереження бвзи в контейнері
docker run --name students -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres

pause
