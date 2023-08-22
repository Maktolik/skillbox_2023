def main():
    sticks_num = int(input('Количество палок: '))
    throws = int(input('Количество бросков: '))

    sticks = ['I'] * sticks_num

    for i in range(throws):
        while True:
            start = int(input('Бросок ' + str(i + 1) + '. Сбиты палки с номера ')) - 1
            if (start >= 0) and (start <= sticks_num):
                break
        while True:
            end = int(input('по номер ')) - 1
            if (end >= start) and (end <= sticks_num):
                break
        for ind in range(start, end + 1):
            sticks[ind] = '.'

    print('Результат: ', sticks)

main()