def main():
    year1 = int(input('Веевиде начальный год: '))
    year2 = int(input('Введите конечный год: '))
    if year1 > year2:
        print('Ошибка , повторите ввод.')
        main()
    while year1 < year2:
        for i in range(10):
            if str(year1).count(str(i)) == 3:
                print(year1)
        year1 += 1

main()