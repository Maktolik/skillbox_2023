import string

notstart = ('@','№','$','%', '^','&')
alwend = ('.txt', '.dxd')

file_name = input('Название файла: ').lower()

if file_name.startswith(notstart):
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(alwend):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')