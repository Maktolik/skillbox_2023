text = open("zen.txt").read().lower()
letters = [c for c in text if c in "abcdefghijklmnopqrstuvwxyz"]
print('Количество букв в файле:{0}\nКоличество слов в файле:{1}\nКоличество строк в файле:{2}\nНаиболее редкая буква:{3}'.format(
    len(letters),
    len(text.split()),
    len(text.split('\n')),
    min(letters, key=letters.count), sep="\n"))