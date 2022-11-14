from text_in_out import text_out
from setting_data import choice_in, set_data, set_search
from getting_data import get_all_data, get_some_data
from record_data import record_column, record_row


def button_click():
    while True:
        data = choice_in()
        match data:
            case '1':
                choice = set_search()
                if choice == 'all':
                    get_all_data(choice)
                else:
                    get_some_data(choice)
            case '2':
                date_list = set_data()
                record_column(date_list)
                record_row(date_list)
            case '0':
                print(text_out())
                break
