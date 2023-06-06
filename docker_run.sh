#!/bin/bash

# Перевіряємо наявність контейнера
if docker ps -a -f name=students | grep -q students; then
    docker rm --force students
    echo "Container \"students\" was deleted."
else
    echo "Container \"students\" not found."
fi

CURRENT_PATH=$(dirname "$0")

# Для збереження бази на хостовій машині
#docker volume create students_data
#docker run --name students -p 5432:5432 -e POSTGRES_PASSWORD=password -v "$CURRENT_PATH/db":/var/lib/postgresql/data -d postgres

# Для збереження бази в контейнері
docker run --name students -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres

