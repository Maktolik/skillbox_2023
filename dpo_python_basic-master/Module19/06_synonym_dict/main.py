def word_sin(dict):
    word = input('\nВведите слово: ').lower().strip()
    if word == 'end':
        return
    elif word in dict:
        print('Синоним:', dict[word])
    else:
        print('Такого слова в словаре нет.')
        word_sin(dict)


def main():
    pairs = int(input('Введите количество пар слов: '))
    text_dict = dict()

    for i in range(1, pairs + 1):
        text = input(f'{i} пара: ').strip(' ').lower().split('-')
        text_dict[text[0].strip(' ')] = text[1].strip(' ')
        text_dict[text[1].strip(' ')] = text[0].strip(' ')

    word_sin(text_dict)


main()
# TODO здесь писать код
