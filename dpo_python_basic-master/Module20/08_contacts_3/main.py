def add_contact(phonebook):
    name = input('Введите имя и фамилию нового контакта: ').split()
    number = input('Введите номер телефона: ')
    res = False
    if len(phonebook) > 0:
        for key, value in phonebook.items():
            first = str(key[0]).lower()
            last = str(key[1]).lower()
            if name[0].lower() == first:
                if name[1].lower() == last:
                    res = True
                    break
    if res == False:
        phonebook[tuple(name)] = number
    else:
        print('Такой человек уже есть в контактах.')


def search_contact(phonebook):
    if len(phonebook) > 0:
        surname = input('Введите фамилию для поиска: ').lower()
        for key, value in phonebook.items():
            last = str(key[1]).lower()
            if surname == last:
                print(key, value)
                main(phonebook)
    else:
        print('Пока нет ни одного контакта ◈')


def main(phonebook):
    menu = 'Введите номер действия:\n1. Добавить контакт\n2. Найти человека\n'
    choice = input(menu)
    if not choice.isdigit():
        choice = 0
    else:
        choice = int(choice)
    if choice == 1:
        add_contact(phonebook)
    elif choice == 2:
        search_contact(phonebook)
    else:
        print('Ошибка ввода. Возврат в главное меню.')
        main(phonebook)
    print('Текущий словарь контактов:', phonebook)
    main(phonebook)


phonebook = {}
main(phonebook)