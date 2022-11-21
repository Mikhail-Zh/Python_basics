import json
import os


def set_student(data_list):
    """Записывает данные ученика в словарь. Пример записи: {'Иванов': (['Иван', '1А'], {})}"""
    student_db[data_list[0]] = data_list[1:], {}


def set_rating(last_name, lesson, rating):
    """Добавление оценок"""
    if student_db.get(last_name) is None:
        print(f'Ученик, с фамилией {last_name} не найден')
    else:
        if lesson in student_db[last_name][1]:
            student_db[last_name][1][lesson].extend(rating)
        else:
            student_db[last_name][1][lesson] = rating


def get_student(last_name_student):
    """Вывод данных ученика"""
    if student_db.get(last_name_student) is None:
        print(f'Ученик, с фамилией {last_name_student} не найден')
    else:
        data = student_db[last_name_student]
        print(f'{last_name_student} {", ".join(data[0])}:')
        print(*[f'{key}: {", ".join(value)}' for key, value in data[1].items()], sep='\n')


def save_db():
    """Сохранение данных учеников из словаря 'student_db' в файл формата .json"""
    json.dump(student_db, open('db_student.json', 'w'))


def load_db():
    """Сохранение данных учеников из файла формата .json в словарь 'student_db'"""
    global student_db
    if os.stat('db_student.json').st_size == 0:
        student_db = {}
    else:
        student_db = json.load(open('db_student.json'))
