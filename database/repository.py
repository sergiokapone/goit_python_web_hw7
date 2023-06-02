"""
У цьому коді визначено функції для виконання операцій CRUD (створення,
читання, оновлення, видалення) на моделях даних, таких як Student, Group,
Teacher, Subject і Grade.
"""

from sqlalchemy import func
from database.models import Student, Group, Teacher, Subject, Grade
from database.db import session


# Функції для моделі Student

def create_student(name, group):
    student = Student(name=name, group=group)
    session.add(student)
    session.commit()
    return student


def get_student(student_id):
    student = session.query(Student).get(student_id)
    return student


def update_student(student_id, new_name):
    student = session.query(Student).get(student_id)
    student.name = new_name
    session.commit()
    return student


def delete_student(student_id):
    student = session.query(Student).get(student_id)
    session.delete(student)
    session.commit()

def list_students():
    students = session.query(Student).all()
    if students:
        for student in students:
            print(f"Student ID: {student.id}, Name: {student.name}")
    else:
        print("No students found.")



# Функції для моделі Group

def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    return group


def get_group(group_id):
    group = session.query(Group).get(group_id)
    return group


def update_group(group_id, new_name):
    group = session.query(Group).get(group_id)
    group.name = new_name
    session.commit()
    return group


def delete_group(group_id):
    group = session.query(Group).get(group_id)
    session.delete(group)
    session.commit()


def list_groups():
    groups = session.query(Group).all()
    if groups:
        for group in groups:
            print(f"Group ID: {group.id}, Name: {group.name}")
    else:
        print("No groups found.")


# Функции для модели Teacher

def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    return teacher


def get_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    return teacher


def update_teacher(teacher_id, new_name):
    teacher = session.query(Teacher).get(teacher_id)
    teacher.name = new_name
    session.commit()
    return teacher


def delete_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    session.delete(teacher)
    session.commit()

def list_teachers():
    teachers = session.query(Teacher).all()
    if teachers:
        for teacher in teachers:
            print(f"Teacher ID: {teacher.id}, Name: {teacher.name}")
    else:
        print("No teachers found.")


# Функции для модели Subject

def create_subject(name, teacher):
    subject = Subject(name=name, teacher=teacher)
    session.add(subject)
    session.commit()
    return subject


def get_subject(subject_id):
    subject = session.query(Subject).get(subject_id)
    return subject


def update_subject(subject_id, new_name):
    subject = session.query(Subject).get(subject_id)
    subject.name = new_name
    session.commit()
    return subject


def delete_subject(subject_id):
    subject = session.query(Subject).get(subject_id)
    session.delete(subject)
    session.commit()

def list_subjects():
    subjects = session.query(Subject).all()
    if subjects:
        for subject in subjects:
            print(f"Teacher ID: {subject.id}, Name: {subject.name}")
    else:
        print("No subjects found.")


# Функции для модели Grade

def create_grade(student, subject, value):
    grade = Grade(student=student, subject=subject, value=value)
    session.add(grade)
    session.commit()
    return grade


def get_grade(grade_id):
    grade = session.query(Grade).get(grade_id)
    return grade


def update_grade(grade_id, new_value):
    grade = session.query(Grade).get(grade_id)
    grade.value = new_value
    session.commit()
    return grade


def delete_grade(grade_id):
    grade = session.query(Grade).get(grade_id)
    session.delete(grade)
    session.commit()


def get_max_students_count():

    max_count = session.query(func.count(Student.id)).scalar()
    return max_count


def get_max_groups_count():

    max_count = session.query(func.count(Group.id)).scalar()
    return max_count


def get_max_teachers_count():

    max_count = session.query(func.count(Teacher.id)).scalar()
    return max_count


def get_max_subjects_count():

    max_count = session.query(func.count(Subject.id)).scalar()
    return max_count


