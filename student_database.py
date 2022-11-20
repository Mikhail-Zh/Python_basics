# Переменная student_db - словарь. В качестве ключа фамилия ученика. Пример: {'Иванов': (['Иван', '1А'], {})}
student_db = {'Иванов': (['Иван', '1А'], {'Физика': ['3', '5', '4']})}


def set_student(data):
    # global student_db
    student_db[data[0]] = data[1:], {}
    print(student_db)


def set_rating(last_name, lesson, rating):
    global student_db
    if student_db.get(last_name) is None:
        print(f'Ученик, с фамилией {last_name} не найден')
    else:
        if lesson in student_db[last_name][1]:
            student_db[last_name][1][lesson].extend(rating)
        else:
            student_db[last_name][1][lesson] = rating


def get_student(last_name_student):
    # global student_db
    if student_db.get(last_name_student) is None:
        print(f'Ученик, с фамилией {last_name_student} не найден')
    else:
        data = student_db[last_name_student]
        print(f'{last_name_student} {", ".join(data[0])}:')
        print(*[f'{key}: {", ".join(value)}' for key, value in data[1].items()], sep='\n')


if __name__ == '__main__':
    print(student_db['Иванов'][1])
