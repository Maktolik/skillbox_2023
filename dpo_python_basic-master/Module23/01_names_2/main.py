def check_len(line_number, line):
    length = len(line)
    if length < 3:
        raise ValueError(f'Ошибка!В строке {line_number+1}: имя менее трех символов')
    return True

def main():
    smb_count = 0

    with (
        open('people.txt', 'r', encoding='utf8') as people_file,
        open('errors.log', 'w', encoding='utf8') as errors_file
    ):

        for line_number, line in enumerate(people_file):
            try:
                strip_line = line.strip()
                if check_len(line_number, strip_line):
                    smb_count += len(strip_line)
            except ValueError as error:
                errors_file.write(str(error))

    print('Общее количество символов:', smb_count)

main()
