from sqlalchemy import func
from database.models import Student, Group, Teacher, Subject, Grade
from database.db import session



# Найти 5 студентов с наибольшим средним баллом по всем предметам
def select_1():
    students = session.query(Student.name).\
        join(Student.grades).\
        group_by(Student).\
        order_by(func.avg(Grade.value).desc()).\
        limit(5).\
        all()
    return students


# Найти студента с наивысшим средним баллом по определенному предмету
def select_2(subject_name):
    student = session.query(Student.name).\
        join(Student.grades).\
        join(Grade.subject).\
        filter(Subject.name == subject_name).\
        group_by(Student).\
        order_by(func.avg(Grade.value).desc()).\
        first()
    return student


# Найти средний балл в группах по определенному предмету
def select_3(subject_name):
    avg_grades = session.query(Group.name, func.avg(Grade.value)).\
        join(Group.students).\
        join(Student.grades).\
        join(Grade.subject).\
        filter(Subject.name == subject_name).\
        group_by(Group).\
        all()
    return avg_grades


# Найти средний балл на потоке (по всей таблице оценок)
def select_4():
    avg_grade = session.query(func.avg(Grade.value)).scalar()
    return avg_grade


# Найти какие курсы читает определенный преподаватель
def select_5(teacher_name):
    courses = session.query(Subject.name).\
        join(Subject.teacher).\
        filter(Teacher.name == teacher_name).\
        all()
    return courses


# Найти список студентов в определенной группе
def select_6(group_name):
    students = session.query(Student).\
        join(Student.group).\
        filter(Group.name == group_name).\
        all()
    return students


# Найти оценки студентов в отдельной группе по определенному предмету
def select_7(group_name, subject_name):
    grades = session.query(Grade).\
        join(Grade.student).\
        join(Grade.subject).\
        join(Student.group).\
        filter(Group.name == group_name, Subject.name == subject_name).\
        all()
    return grades


# Найти средний балл, который ставит определенный преподаватель по своим предметам
def select_8(teacher_name):
    avg_grade = session.query(func.avg(Grade.value)).\
        join(Grade.subject).\
        join(Subject.teacher).\
        filter(Teacher.name == teacher_name).\
        scalar()
    return avg_grade


# Найти список курсов, которые посещает определенный студент
def select_9(student_name):
    courses = session.query(Subject.name).\
        join(Subject.grades).\
        join(Grade.student).\
        filter(Student.name == student_name).\
        all()
    return courses


# Список курсов, которые определенному студенту читает определенный преподаватель
def select_10(student_name, teacher_name):
    courses = session.query(Subject.name).\
        join(Subject.teacher).\
        join(Subject.grades).\
        join(Grade.student).\
        filter(Student.name == student_name, Teacher.name == teacher_name).\
        all()
    return courses




def execute_query(query_func, *args):
    # Установка соединения с базой данных
    db_session = session

    # Выполнение запроса
    result = query_func(*args)

    # Закрытие соединения с базой данных
    db_session.close()

    # Возврат результата
    return result



if __name__ == '__main__':
    
    queries = [
        (select_1,),
        (select_2, "Математика"),
        (select_3, "Фізика"),
        (select_4,),
        (select_5, "Иванов"),
        (select_6, "Группа 1"),
        (select_7, "Группа 2", "История"),
        (select_8, "Петров"),
        (select_9, "Иванов"),
        (select_10,),
    ]




    print(execute_query(select_3, "Математика"))



