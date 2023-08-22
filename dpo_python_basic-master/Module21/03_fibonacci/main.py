def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {fib(number)}')
