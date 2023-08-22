def main():
    number_list = []
    number = int(input('Введите целое число: '))
    for i in range(1, number + 1):
        if i % 2 != 0:
            number_list.append(i)
    print('Список из нечётных чисел от 1 до N:', number_list)

main()
