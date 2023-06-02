# Домашнє завдання #7

Робота з базою [`PostgreSQL`](https://www.postgresql.org/)[^1] за допомогою [`ORM SQLAlchemy`](https://www.sqlalchemy.org/)[^2].

[^1]: `PostgreSQL` (або просто `Postgres`) - це потужна об'єктно-реляційна система управління базами даних (СУБД), що забезпечує збереження, організацію та маніпулювання даними. Вона є одним із найпопулярніших відкритих реляційних баз даних.
[^2]: `Object-Relational Mapping` - Технологія програмування, яка пов'язує бази даних із концепціями об'єктно-орієнтованих мов програмування, створюючи "віртуальну об'єктну базу даних".

## Запуск проекта

Для запуску проекта `pipenv install` або `pipenv sync`.

## Запуск бази данних

Для запуску бази данних запустіть файл `docker_run.cmd`, або команду `docker run --name students -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres`.

## Створення міграцій

Для створення міграцій скористайтесь файлом `alembic.cmd`.
Меню скрипта має вигляд:

```text
1. Згенерувати міграцію
2. Застосувати всі міграції
3. Відкотити останню міграцію
4. Переглянути поточний стан міграцій
5. Вийти
```

## Сртуктура проекту

```text
.
├── alembic/
│   └── versions/           # Директорія з файлами міграцій
├── database/
│   ├── db.py               # Код для керування підключенням до бази даних
│   ├── models.py           # Визначення моделей даних
│   └── repository.py       # Код виконання операцій CRUD
├── .gitignore
├── Pipfile
├── alembic.cmd             # Робота з міграціями
├── docker_run.cmd          # Запуск контейнера з базою даних
├── alembic.ini             # Налаштування alembic
├── config.ini              # Налаштування для підключення до бази даних
├── Pipfile.lock
├── README.MD
├── main.py                 # Код CLI для операцій CRUD
├── my_select.py            # Код для запитів до бази даних
└── seed.py                 # Код для заповнення бази даних початковими даними
```

## CLI для CRUD

```bash
usage: main.py [-h] [--action ACTION] [--model MODEL] [--id ID] [--name NAME] [--subject SUBJECT] [--value VALUE]

Students DB

options:
  -h, --help            show this help message and exit
  --action ACTION, -a ACTION
                        Commands: create, update, get, remove, list
  --model MODEL, -m MODEL
                        Models: Teacher, Group, Student, Subject, Grade
  --id ID               ID of the object
  --name NAME, -n NAME  Name of the object
  --subject SUBJECT, -s SUBJECT
                        Subject of the object
  --value VALUE, -v VALUE
                        Value of the object
```

### Приклади виконання команд у терміналі.

- Показати всіх вчителів: `python main.py -a list -m Teacher`
- Створити вчителя: `python main.py -a create -m Teacher -n "Mister X"`
- Ооновити дані вчителя з `id=3`: `python main.py -a update -m Teacher --id 3 -name "Andry Bezos" `
- Показати всі групи: `python main.py -a list -m Group`
- Створити групу: `python main.py -a create -m Group -n "AD-101"`
- ...

## Допоміжний софт

Для роботи з базою данних сожна використати [HeidiSQL](https://www.heidisql.com/download.php)

`HeidiSQL` дозволяє переглядати і редагувати дані і структури з комп'ютерів, на яких працює одна з систем баз даних `MariaDB`, `MySQL`, `Microsoft SQL`, `PostgreSQL` і `SQLite`.
