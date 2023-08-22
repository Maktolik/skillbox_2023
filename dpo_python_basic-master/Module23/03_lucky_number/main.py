import random

def chance_to_end():
    res = True
    chance = random.randint(1, 13)
    if chance == 13:
        res = False
    return res
def save_number(num):
        file.write(str(num) + '\n')


final = 777
sum_num = 0
file_name = 'out_file.txt'
first_record = True
with open(file_name, 'w', encoding='utf8') as file:
    while True:
        new_num = int(input('Введите число: '))
        sum_num += new_num
        if sum_num >= final:
            print('Вы успешно выполнили условие для выхода из порочного круга!')
            save_number(new_num)
            break

        if chance_to_end():
            save_number(new_num)
        else:
            try:
                rnd_except = random.randint(1, 5)
                if rnd_except == 1:
                    raise IndexError('Ошибка 404.')
                elif rnd_except == 2:
                    raise GeneratorExit('Ошибка ввода даных')
                elif rnd_except == 3:
                    raise ArithmeticError('CWE-73: External Control of File Name or Path ')
                elif rnd_except == 4:
                    raise FloatingPointError('CWE-682: Incorrect Calculation')
                elif rnd_except == 5:
                    raise ZeroDivisionError('CWE-330: Use of Insufficiently Random Values')
            except Exception as err:
                print(err)
            break