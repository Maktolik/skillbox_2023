

text = input('Сообщение: ').split()
word_rev = ''
for word in text:
    word_part = ''
    for lat in word:
        if lat.isalpha():
            word_part = lat + word_part
        else:
            word_rev += word_part + lat + ''
            word_part = ''
    word_rev += word_part + ' '

print('Новое сообщение:', word_rev)