def revers_num(num):
    x = int(num)
    n = 0

    while x > 0:
        digit = x % 10
        x = x // 10
        n = n * 10
        n = n + digit

    y = ''
    for i in reversed(str(num)):
        if i == '.':
            break
        y = y + i
    y = float('0.' + y)
    return n + y

def main():
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))

    print(f'Первое число наоборот: {revers_num(num1)}')
    print(f'Второе число наоборот: {revers_num(num2)}')
    print(f'Сумма: {revers_num(num1) + revers_num(num2)}')

main()




