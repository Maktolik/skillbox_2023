import random

def main():
    numbers = int(input('Количество чисел в списке: '))

    start = [random.randint(0, 2) for _ in range(numbers)]
    press = [x for x in start if x > 0]
    count = len(start) - len(press)
    end = press[:] + [0 for _ in range(count)]

    print('Случайный список:', start)
#    print('Список до сжатия:', end)
    print('Список после сжатия:', press)

main()