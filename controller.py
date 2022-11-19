from teacher import add_student, put_rating
from student import see_rating


def controller():
    match input('Укажите себя. 1 - учитель, 2 - ученик: '):
        case '1':
            print('Что хотите сделать?')
            act = input('1 - записать ученика, 2 - выставить оценку\nВвод: ')
            if act == '1':
                add_student()
            elif act == '2':
                put_rating()
        case '2':
            print(see_rating())
