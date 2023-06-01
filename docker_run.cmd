@echo off
REM Проверяем наличие контейнера
docker ps -a -f name=students | findstr students
IF %ERRORLEVEL% EQU 0 (
    REM Контейнер присутствует, удаляем его
    docker rm --force students
    echo Container "students" was deleted.
) ELSE (
    REM Контейнер отсутствует
    echo Container "students" not found.
)

REM Запускаем новый контейнер
docker run --name students -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
