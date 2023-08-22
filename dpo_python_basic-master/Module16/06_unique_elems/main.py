def main():
    list_one = []
    list_two = []

    for i in range(3):
        num = int(input('Введите ' + str(i + 1) + ' число для первого списка: '))
        list_one.append(num)

    for i in range(7):
        num = int(input('Введите ' + str(i + 1) + ' число для второго списка: '))
        list_two.append(num)

    list_one.extend(list_two)
    for _ in range(len(list_one)):
        for i in list_one:
            if list_one.count(i) > 1:
                list_one.remove(i)

    print(list_one)

main()