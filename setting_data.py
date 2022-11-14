from text_in_out import text_in, text_in_start, text_search_start


def choice_in():
    print(text_in_start())
    data = input('Ввод: ')
    return data


def set_data():
    return input(text_in()).split(',')


def set_search():
    print(text_search_start())
    choice_search = input('Ввод: ')
    return choice_search
