from student_database import set_student, set_rating


def add_student():
    metric = input('Введите данные: ')
    set_student(metric)


def put_rating():
    set_rating('1')
