from sqlalchemy import func
from database.models import Student, Group, Teacher, Subject, Grade
from database.db import session



def select_1():
    """ Знайти 5 студентів з найбільшим середнім балом по всім предметам"""

    students = session.query(Student.name, func.avg(Grade.value)).\
        join(Student.grades).\
        group_by(Student).\
        order_by(func.avg(Grade.value).desc()).\
        limit(5).\
        all()
    return students



def select_2(subject_name):
    """Знайти студента із найвищим середнім балом з певного предмета."""

    student = session.query(Student.name, Subject.name, func.avg(Grade.value)).\
        join(Student.grades).\
        join(Grade.subject).\
        filter(Subject.name == subject_name).\
        group_by(Student, Subject).\
        order_by(func.avg(Grade.value).desc()).\
        first()
    return student






def select_3(subject_name):
    """Знайти середній бал у групах з певного предмета."""

    avg_grades = session.query(Group.name, Subject.name, func.avg(Grade.value)).\
        join(Group.students).\
        join(Student.grades).\
        join(Grade.subject).\
        group_by(Subject).\
        filter(Subject.name == subject_name).\
        group_by(Group).\
        all()
    return avg_grades



def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""

    avg_grade = session.query(func.avg(Grade.value)).scalar()
    return avg_grade



def select_5(teacher_name):
    """Знайти які курси читає певний викладач."""

    courses = session.query(Subject.name).\
        join(Subject.teacher).\
        filter(Teacher.name == teacher_name).\
        all()
    return courses



def select_6(group_name):
    """Знайти список студентів у певній групі."""

    students = session.query(Student.name).\
        join(Student.group).\
        filter(Group.name == group_name).\
        all()
    return students


def select_7(group_name, subject_name):
    """Знайти оцінки студентів у окремій групі з певного предмета."""

    grades = session.query(Group.name , Student.name, Subject.name, Grade.value).\
        join(Grade.student).\
        join(Grade.subject).\
        join(Student.group).\
        filter(Group.name == group_name, Subject.name == subject_name).\
        all()
    return grades



def select_8(teacher_name):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    avg_grade = session.query(func.avg(Grade.value)).\
        join(Grade.subject).\
        join(Subject.teacher).\
        filter(Teacher.name == teacher_name).\
        scalar()
    return avg_grade



def select_9(student_name):
    """Знайти список курсів, які відвідує певний студент."""

    courses = session.query(Subject.name).\
        join(Subject.grades).\
        join(Grade.student).\
        filter(Student.name == student_name).\
        all()
    return courses



def select_10(student_name, teacher_name):
    """Список курсів, які певному студенту читає певний викладач."""

    courses = session.query(Subject.name).\
        join(Subject.teacher).\
        join(Subject.grades).\
        join(Grade.student).\
        filter(Student.name == student_name, Teacher.name == teacher_name).\
        all()
    return courses


def select_11(teacher_name, student_name):
    """Середній бал, який певний викладач ставить певному студентові."""

    avg_grade = session.query(func.avg(Grade.value)).\
        join(Grade.student).\
        join(Grade.subject).\
        join(Subject.teacher).\
        filter(Teacher.name == teacher_name).\
        filter(Student.name == student_name).\
        scalar()
    return avg_grade


def select_12(group_name, subject_name):
    """Оцінки студентів у певній групі з певного предмета на останньому занятті."""

    grades = session.query(Student.name, Grade.value).\
        join(Grade.student).\
        join(Grade.subject).\
        join(Subject.teacher).\
        join(Student.group).\
        filter(Group.name == group_name).\
        filter(Subject.name == subject_name).\
        order_by(Grade.created_at.desc()).\
        all()
    return grades




def execute_query(query_func, *args):
    # З'єднання з базою даних
    db_session = session

    # Виконання запиту
    result = query_func(*args)

    # закриття сесії
    db_session.close()

    return result



if __name__ == '__main__':
    
    queries = [
        (select_1,),
        (select_2, "Математика"),
        (select_3, "Фізика"),
        (select_4,),
        (select_5, "Алевтин Сірко"),
        (select_6, "ФФ-11"),
        (select_7, "ФФ-12", "Фізика"),
        (select_8, "Соломон Євдокименко"),
        (select_9, "Юхим Лагода"),
        (select_10, "Ада Ґереґа", "Соломон Євдокименко"),
        (select_11, "Алевтин Сірко", "Сніжана Хоменко"),
        (select_12, "ФФ-13", "Фізика"),
    ]




    # Виклик функції execute_query для кожного запиту
    for i, query in enumerate(queries):
        docstring = query[0].__doc__
        print(f"{i+1}: {docstring}\n")
        print(f"Результат: {execute_query(*query)}")
        print("="*79)

