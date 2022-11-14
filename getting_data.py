from text_in_out import missing_data


def get_all_data(elem):
    with open('phone_dir_row.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').rstrip(';').split(',')
            print(*line)


def get_some_data(elem):
    with open('phone_dir_row.txt', 'r', encoding='utf-8') as f:
        cnt = 0
        for line in f:
            line = line.strip('\n').rstrip(';').split(',')
            if elem in line:
                cnt += 1
                print(*line)
        if not cnt:
            print(missing_data())
