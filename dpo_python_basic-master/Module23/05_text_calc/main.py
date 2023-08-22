with open('calc.txt') as file:
    res = 0
    for line in file:
        try:
            line = line.replace('\n', '')
            line_values = line.split(' ')
            if line_values[1] == '+':
                res = float(line_values[0])+float(line_values[2])
            elif line_values[1] == '-':
                res = float(line_values[0])-float(line_values[2])
            elif line_values[1] == '*':
                res = float(line_values[0])*float(line_values[2])
            elif line_values[1] == '/':
                res = float(line_values[0])/float(line_values[2])
            else:
                raise BaseException()
            print(f'Результат {line}: {res}')
        except BaseException:
            print(f'Результат {line}: Ошибка: Неизвестная арифметическая операция')