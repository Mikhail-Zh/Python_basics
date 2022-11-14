def record_column(data):
    with open('phone_dir_column.txt', 'a', encoding='utf-8') as f:
        for i in data:
            f.writelines(f'{i}\n')
        f.writelines(f'\n')


def record_row(data):
    with open('phone_dir_row.txt', 'a', encoding='utf-8') as f:
        f.writelines(f"{','.join(data)};\n")
