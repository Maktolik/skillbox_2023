def main():
    rolers = []
    foot_size = []
    count = 0

    num = int(input('Кол-во коньков: '))
    for i in range(num):
        size = int(input('Размер ' + str(i + 1) + ' пары: '))
        rolers.append(size)

    num = int(input('\nКол-во людей: '))

    for i in range(num):
        size = int(input('Размер ноги ' + str(i + 1) + ' человека: '))
        foot_size.append(size)

    for foot in foot_size:
        if foot in rolers:
            rolers.remove(foot)
            count += 1
    print('Наибольшее кол-во людей, которые могут взять ролики:', count)


main()
