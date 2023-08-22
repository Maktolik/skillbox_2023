count = 0
string = ''

with open('numbers.txt') as file:
    for row in file.readlines():
        string = row.strip()
        if string != '':
            count += int(string)

f = open('answer.txt', 'w')
f.write(str(count))
f.close()