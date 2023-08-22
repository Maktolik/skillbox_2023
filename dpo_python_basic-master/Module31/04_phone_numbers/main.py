import re

numbers = ['9999999999', '999999-999', '99999x9999']
names_list = ['первый номер:', 'второй номер:', 'третий номер:']
for number, name in zip(numbers, names_list):
    if re.fullmatch(r'[89]\d{9}', number):
        print(f'{name} : всё в порядке')
    else:
        print(f'{name} : не подходит')