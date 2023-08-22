text = input('Введите строку: ').split()
max_lengh = 0
max_word = ''

word = [len(i) for i in text]
larg = text[word.index(max(word))]

print('Самое длинное слово:', larg)
print('Длина этого слова:', len(larg))