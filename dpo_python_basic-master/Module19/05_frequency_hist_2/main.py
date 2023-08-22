text = input('Введите текст: ')
symb_dict = dict()
text_dict = dict()

print('Оригинальный словарь частот:')
for symb in text:
    if symb in symb_dict:
        symb_dict[symb] += 1
    else:
        symb_dict[symb] = 1
for i_symb in sorted(symb_dict.keys()):
    print(i_symb, ': ', symb_dict[i_symb])

print('Инвертированный словарь частот:')
for i_let, i_num in symb_dict.items():
    text_dict.setdefault(i_num, []).append(i_let)
for i in text_dict:
    print(i, ': ', text_dict[i])
