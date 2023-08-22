str_1 = input('Первая строка: ')
str_2 = input('Вторая строка: ')
str_1_for_find = 2 * str_1
possibility = str_1_for_find.find(str_2)
if possibility < 0:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    print(f'Первая строка получается из второй со сдвигом {possibility}.')
