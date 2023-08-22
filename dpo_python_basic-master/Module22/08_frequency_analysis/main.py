ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

text = open('text.txt', 'r').read().lower()
dict = {}
count = 0
for i_let in text:
    if i_let in ascii:
        x = dict.get(i_let, 0)
        dict[i_let] = x + 1
        count += 1

sort_dict = sorted(dict)
analis = [[i_el, round((dict[i_el] / count), 3)] for i_el in sort_dict]
analysis = '\n'.join([i_el[0] + ' ' + str(i_el[1]) for i_el in analis])
open('analysis.txt', 'w').write(analysis)