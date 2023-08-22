def main():
    number = int(input('Кол-во контейнеров: '))
    contain = []
    row = 0
    for i in range(number):
        while True:
            weight = int(input('Введите вес ' + str(i + 1) + ' контейнера: '))
            if weight <= 200:
                break
        contain.append(weight)
    contain.sort(reverse=True)
    new_weight = int(input('Введите вес для нового контейнера: '))
    for ind in range(len(contain)):
        row = ind + 1
        if contain[ind] < new_weight:
            break
    print('Номер, который получит новый контейнер:', row)


main()

