#skill Module22 05_save
import os

text = str(input('Введите строку: \n'))
way = str(input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): \n'))
filename = str(input('Введите имя файла: \n'))

normpath = way.replace(" ", "/")
path = str('C:/' + normpath)
r_path = str(normpath + "/" + filename)
abs_path = os.path.abspath(filename)
check_file = os.path.exists(abs_path)

if check_file:
    ans = input('Вы действительно хотите перезаписать файл? \n')
    if ans == 'да':
        with open(filename, 'w') as file:
            file.write(text)
            print('Файл успешно перезаписан!')
    else:
        print('Файл не был записан')
else:
    with open(filename, 'w') as file:
        file.write(text)
        print('Файл успешно сохранён!')