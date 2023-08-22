def main():
    friend = int(input('Кол-во друзей: '))
    rac = int(input('Долговых расписок: '))
    frd_list = []

    for _ in range(friend):
        frd_list.append(0)

    for num in range(rac):
        print(f'\n{num + 1} расписка')
        whom = int(input('Кому: '))
        who = int(input('От кого: '))
        what = int(input('Сколько: '))
        frd_list[who - 1] += what
        frd_list[whom - 1] -= what

    print('\nБаланс друзей:')
    for i in range(len(frd_list)):
        print(f'{i + 1} : {frd_list[i]}')

main()