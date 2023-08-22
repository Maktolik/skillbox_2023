def str_check(str):
    err_str = str.split()
    if len(err_str) != 3:
        raise ValueError(f'Ошибка в строке: {err_str}! Данные веедены неверно')
    name, mail, age = str.split()
    smb = ("@", ".")
    if age.isdigit() is False:
        raise NameError(f'Ошибка в строке: {err_str}! Поле «Возраст» НЕ является числом')
    elif name.isalpha() is False:
        raise NameError(f'Ошибка в строке: {err_str} Поле «Имя» содержит НЕ только буквы')
    elif int(age) not in range(10, 100):
        raise ValueError(f'Ошибка в строке: {err_str}! Поле «Возраст» НЕ является числом от 10 до 99')
    else:
        for char in smb:
            if char not in mail:
                raise SyntaxError(f'Ошибка в строке: {err_str}! Поле «Имейл» НЕ содержит @ и .')
    return str

with (
    open("registrations.txt", "r", encoding='utf-8') as file_reg,
    open('registration_bad.log', 'w', encoding='utf-8') as file_error,
    open('registrations_good.log', 'w', encoding='utf-8') as file_good
):
    for row in file_reg:
        #print(row, end='')
        try:
            str_add = str_check(row)
        except (NameError, ValueError, SyntaxError) as err:
            file_error.write(str(err)+'\n')
        else:
            file_good.write(str_add)