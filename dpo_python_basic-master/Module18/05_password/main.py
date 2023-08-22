def main():
    password = input('Придумайте пароль: ')
    pass_len = len(password)
    fig_count = 0
    for i in password:
        if i.isdigit():
            fig_count += 1

    if (pass_len < 8) or (password.lower() == password) or (fig_count < 3):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        main()
    else:
        print('Это надёжный пароль!')

main()