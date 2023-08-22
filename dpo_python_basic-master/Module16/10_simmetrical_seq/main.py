def main():
    num = int(input('Кол-во чисел: '))
    lst = []

    for i in range(num):
        lst.append(int(input('Число: ')))

    count = 0
    print('Последовательность:', lst)
    while lst != lst[::-1]:
        lst.insert(num, lst[count])
        count += 1
    print('Нужно приписать чисел:', count)
    print('Сами числа:', lst[:count][::-1])
    print('Симметричная последовательность:', lst)

main()