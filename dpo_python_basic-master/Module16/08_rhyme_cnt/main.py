def main():
    people = int(input('Кол-во человек: '))
    losed = int(input('Какое число в считалке? '))
    print('Значит, выбывает каждый', losed, 'человек.')
    pep_list = list(range(1, people + 1))
    outed = 0

    for _ in range(people - 1):
        print('\nТекущий круг людей', pep_list)
        start = outed % len(pep_list)
        outed = (start + losed - 1) % len(pep_list)
        print('Начало счёта с номера', pep_list[start])
        print('Выбывает человек под номером', pep_list[outed])
        pep_list.remove(pep_list[outed])

    print('\nОстался человек под номером', pep_list)

main()