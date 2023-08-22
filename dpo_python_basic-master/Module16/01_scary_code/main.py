def main():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]

    a.extend(b)
    count_five = a.count(5)
    print('Кол-во цифр 5 при первом объединении:', count_five)
    for _ in range(count_five):
        a.remove(5)

    a.extend(c)
    count_three = a.count(3)
    print('Кол-во цифр 3 при втором объединении:', count_three)

    print('Итоговый список:', a)

main()
