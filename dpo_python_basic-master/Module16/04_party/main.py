def main():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

    todo = ''
    while True:
        print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
        todo = input('Гость пришел или ушел? ').lower()
        if todo == 'пора спать':
            break
        guest_name = input('Имя гостя: ')
        if todo == 'пришел':
            if len(guests) >= 6:
                print(f'Прости, {guest_name}, но мест нет.')
            else:
                guests.append(guest_name)
                print(f'Привет, {guest_name}!')
        elif todo == 'ушел':
            guests.remove(guest_name)
            print(f'Пока, {guest_name}!')
        print()

    print('\nВечеринка закончилась, все легли спать.')

main()
