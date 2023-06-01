"""
У цьому коді визначено функції для виконання операцій CRUD (створення,
читання, оновлення, видалення) на моделях даних, таких як Student, Group,
Teacher, Subject і Grade.
"""

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
