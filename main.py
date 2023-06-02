import logging
from argparse import ArgumentParser
from database.repository import *


# Создание парсера аргументов командной строки
parser = ArgumentParser(description='Students DB')
parser.add_argument('--action', '-a', help='Commands: create, get, update, remove, list')
parser.add_argument('--model', '-m', help='Models: Teacher, Group, Student, Subject, Grade')
parser.add_argument('--id', help='ID of the object')
parser.add_argument('--name', '-n', help='Name of the object')
parser.add_argument('--subject', '-s', help='Subject of the object')
parser.add_argument('--value', '-v', help='Value of the object')

# Парсинг аргументов командной строки
arguments = parser.parse_args()
my_args = vars(arguments)

action = my_args.get('action')
model = my_args.get('model')
id = my_args.get('id')
name = my_args.get('name')
subject = my_args.get('subject')
value = my_args.get('value')


# Конфигурация логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Определение функций для CRUD операций

def create():
    try:
        if not name:
            raise ValueError('Name parameter is missing')

        match model:
            case 'Teacher': 
                create_teacher(name)
                logging.info('Teacher created: %s', name)
            case 'Group': 
                create_group(name)
                logging.info('Group created: %s', name)
            case 'Student':
                create_student(name)
                logging.info('Student created: %s', name)
            case 'Subject':
                teacher = get_teacher(id)
                create_subject(name, teacher)
                logging.info('Subject created: %s', name)
            case 'Grade':
                student = get_student(id)
                subject = get_subject(subject)
                create_grade(student, subject, value)
                logging.info('Grade created for student ID %s and subject ID %s', id, subject)
    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Error occurred during create operation: %s', str(e))

def update():
    try:
        if not model:
            raise ValueError('Model parameter is missing')
        
        if not id:
            raise ValueError('ID parameter is missing')
        
        match model:
            case 'Teacher':
                update_teacher(id, name)
                logging.info('Teacher updated: ID %s, new name: %s', id, name)
            case 'Group':
                update_group(id, name)
                logging.info('Group updated: ID %s, new name: %s', id, name)
            case 'Student':
                update_student(id, name)
                logging.info('Student updated: ID %s, new name: %s', id, name)
            case 'Subject':
                update_subject(id, name)
                logging.info('Subject updated: ID %s, new name: %s', id, name)
            case 'Grade':
                update_grade(id, value)
                logging.info('Grade updated: ID %s, new value: %s', id, value)

    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Error occurred during update operation: %s', str(e))

def remove():
    try:

        if not id:
            raise ValueError('ID parameter is missing')
        
        match model:
            case 'Teacher':
                delete_teacher(id)
                logging.info('Teacher deleted: ID %s', id)
            case 'Group':
                delete_group(id)
                logging.info('Group deleted: ID %s', id)
            case 'Student':
                delete_student(id)
                logging.info('Student deleted: ID %s', id)
            case 'Subject':
                delete_subject(id)
                logging.info('Subject deleted: ID %s', id)
            case 'Grade':
                delete_grade(id)
                logging.info('Grade deleted: ID %s', id)

    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Error occurred during remove operation: %s', str(e))

def get():
    try:

        if not id:
            raise ValueError('ID parameter is missing')

        match model:
            case 'Teacher':
                teacher = get_teacher(id)
                logging.info('Teacher details: ID %s, Name: %s', id, teacher.name)
            case 'Group':
                group = get_group(id)
                logging.info('Group details: ID %s, Name: %s', id, group.name)
            case 'Student':
                student = get_student(id)
                logging.info('Student details: ID %s, Name: %s', id, student.name)
            case 'Subject':
                subject = get_subject(id)
                logging.info('Subject details: ID %s, Name: %s', id, subject.name)
            case 'Grade':
                grade = get_grade(id)
                logging.info('Grade details: ID %s, Value: %s', id, grade.value)

    except ValueError as ve:
        logging.error('ValueError: %s', str(ve))
    except Exception as e:
        logging.error('Error occurred during get operation: %s', str(e))

def list_():
    try:

        match model:
            case 'Teacher':
                list_teachers()
            case 'Group':
                list_groups()
            case 'Student':
                list_students()
            case 'Subject':
                list_subjects()
            case 'Grade':
                list_grades()

    except Exception as e:
        logging.error('Error occurred during get operation: %s', str(e))

# Виклик відповідної функції залежно від команди
match action:
    case 'create':
        create()
    case 'update':
        update()
    case 'remove':
        remove()
    case 'get':
        get()
    case 'list':
        list_()
    case _:
        parser.print_help()
