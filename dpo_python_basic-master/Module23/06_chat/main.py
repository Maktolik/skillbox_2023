
def main():
    user = input('Введите имя: ')

    while True:
        print('1 - посмотреть текущий текст чата\n2 - отправить сообщение')
        action = input()

        if action == '1':
            try:
                with open('chat.txt', 'r', encoding='utf-8') as file:
                    for i_mess in file:
                        print(i_mess, end='')
            except FileNotFoundError:
                print('История сообщений пуста. \n')
        elif action == '2':
            mess = input('Введите сообщение: ')
            with open('chat.txt', 'a+', encoding='utf-8') as file:
                file.write(f'{user}: {mess}\n')
        else:
            print('Неверная команда, возвращаю в меню.')
            main()

main()