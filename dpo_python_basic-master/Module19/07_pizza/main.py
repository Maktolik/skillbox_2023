num_orders = int(input('Введите кол-во заказов: '))
data = dict()

for i in range(0, num_orders):
    order = input(f'{i + 1} заказ: ').lower().split()
    if order[0] not in data:
        data[order[0]] = {order[1]: int(order[2])}
    else:
        if order[1] not in data[order[0]]:
            data[order[0]][order[1]] = int(order[2])
        else:
            data[order[0]][order[1]] += int(order[2])

# print(data)
for i in sorted(data.keys()):
    print(i.title(), ':')
    for ind in sorted(data[i].keys()):
        print('    ', ind.title(), ':', data[i][ind])