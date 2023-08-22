import random

def f1(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError('Ошибка в функции №1')
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise ZeroDivisionError('Ошибка в функции №2')
    return y / x


def main():
    with (
        open('coordinates.txt', 'r', encoding='utf8') as coord_file,
        open('result.txt', 'w', encoding='utf8') as res_file
    ):
        for i_row, row in enumerate(coord_file):
            numbers = row.split()
            x = int(numbers[0])
            y = int(numbers[1])
            try:
                number = random.randint(0, 100)
                res_to_write = sorted([f1(x,y), f2(x, y), number])
                res_file.write(str(res_to_write)+'\n')
            except ZeroDivisionError as error:
                res_file.write(str(error)+'\n')

main()