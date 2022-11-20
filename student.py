from student_database import get_student


def see_rating():
    last_name = input('Введите фамилию: ')
    get_student(last_name)
