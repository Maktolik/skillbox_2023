people_num = int(input('Введите количество человек: '))
data_dict = dict()
lvl_dict = dict()
for i in range(1, people_num):
    name, parent_name = input(f'{i} пара: ').split()
    data_dict[name] = parent_name
    lvl_dict[name] = 0
    lvl_dict[parent_name] = 0

for ind in data_dict:
    people = ind
    while people in data_dict:
        people = data_dict[people]
        lvl_dict[ind] += 1

print('\n“Высота” каждого члена семьи:')
for i in sorted(lvl_dict):
    print(i, lvl_dict[i])
