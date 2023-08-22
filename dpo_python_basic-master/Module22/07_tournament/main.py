new_lst = []

with open('first_tour.txt') as file:
    scor = int(file.readline())
    for line in file:
        new_line = line.split()
        if new_line != [] and int(new_line[-1]) > scor:
            new_lst.append(new_line)

new_lst.sort(key=lambda a: int(a[-1]))
new_lst.reverse()

count = str(len(new_lst))

sec_lst = []
n = 1
for i in new_lst:
    name= str(i[0][0]) + '.'
    win = str(n) + ') ' + name + ' ' + i[1] + ' ' + i[-1]
    sec_lst.append(win)
    n += 1

with open("second_tour.txt", "w") as file_wr:
    file_wr.write(count + '\n')
    s = '\n'.join(sec_lst)
    file_wr.write(s)

for i in sec_lst:
    print(f'{i}')