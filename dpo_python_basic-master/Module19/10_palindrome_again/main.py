word = input('Введите строку: ').lower()
symb = set()

for i in word:
    if i in symb:
        symb.remove(i)
    else:
        symb.add(i)
if len(symb) > 1:
    print('Нельзя сделать полиндром')
else:
    print('Можно сделать полиндром')
