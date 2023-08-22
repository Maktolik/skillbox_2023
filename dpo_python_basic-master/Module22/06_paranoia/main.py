import os
def get_index(num, to_rb, lst):
    ind = lst.index(num)
    if ind + to_rb > len(lst) - 1:
        ind = ind + to_rb - len(lst)
    else:
        ind += to_rb
    return ind


path = os.path.abspath('text.txt')
f = open(path, 'r')
count = 0
string = ''
ascii = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for row in f:
    count += 1

    for smb in row:
        if smb in ascii:
            string += ascii[get_index(smb, count, ascii)]
        else:
            string += smb

f.close()

path = os.path.abspath('cipher_text.txt')
f = open(path, 'w')
f.write(string)
f.close()
