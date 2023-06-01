from faker import Faker
from database.models import Student, Group, Teacher, Subject, Grade
from database.db import session


fake = Faker("uk_UA")

# Створюємо 3 групи
groups = []
for _ in range(3):
    group = Group(name=fake.word())
    groups.append(group)
    session.add(group)

# Створюємо 5-8 предметів та 3-5 викладачів
teachers = []
subjects = []
for _ in range(fake.random_int(min=5, max=8)):
    teacher = Teacher(name=fake.name())
    teachers.append(teacher)
    session.add(teacher)

    subject = Subject(name=fake.word(), teacher=teacher)
    subjects.append(subject)
    session.add(subject)

# Створюємо 30-50 студентів
students = []
for _ in range(fake.random_int(min=30, max=50)):
    student = Student(name=fake.name(), group=fake.random_element(groups))
    students.append(student)
    session.add(student)

    # Додаємо до 20 оцінок кожному студенту за всі предмети
    for subject in subjects:
        for _ in range(fake.random_int(min=1, max=20)):
            grade = Grade(
                student=student,
                subject=subject,
                value=fake.random_int(min=1, max=100)
            )
            session.add(grade)

# Зберігаємо зміни в базі даних
session.commit()

print("Дані було успішно згенеровано і додано до бази даних.")
