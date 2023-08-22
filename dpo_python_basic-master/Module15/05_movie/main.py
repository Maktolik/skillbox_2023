films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']


def search_mov(list_f, mov):
    res = 0
    for i in range(len(list_f)):
        if list_f[i] == mov:
            res = i
            break
    return res


def main():
    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
              'Леон', 'Богемская рапсодия', 'Город грехов',
              'Мементо', 'Отступники', 'Деревня']
    favor_films = []
    add_films = int(input('Сколько фильмов хотите добавить? '))
    for i in range(add_films):
        mov = input('Введите название фильма: ')
        mov_have = search_mov(films, mov)
        if mov_have > 0:
            favor_films.append(mov)
        else:
            print('Ошибка: фильма', mov, 'у нас нет :(')
    print('Ваш список любимых фильмов:', favor_films)



main()