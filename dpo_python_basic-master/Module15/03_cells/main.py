def main():
    cell = [3, 0, 6, 2, 10]
    cell_used = []
    unsuit = ''
    print('Количество клеток:', len(cell))
    for i in range(0, len(cell)):
        print('Эффективность', i + 1, 'клетки:', cell[i])
        if i > cell[i]:
            cell_used.append(cell[i])
    if len(cell_used) > 0:
        for ind in range(0, len(cell_used)):
            unsuit += str(cell_used[ind]) + ' '
        print('Неподходящие значения:', unsuit)


main()
