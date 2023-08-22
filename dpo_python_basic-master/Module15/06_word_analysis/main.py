def main():
    word = input('Введите слово: ').lower()
    uniq = 0
    for letter in word:
        count = 0
        for i in word:
            if letter == i:
                count += 1
        if count == 1:
            uniq += 1
    print('Количество уникальных букв в слове:', uniq)


main()

