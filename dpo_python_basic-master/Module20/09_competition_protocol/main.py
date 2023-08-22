def score(x_score):
    return x_score[1][0] * 100000000 - x_score[1][1]


table = {}
rows = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
for time in range(rows):
    ball, name = input(f' {time + 1} запись: ').split()
    ball = int(ball)
    if name in table:
        if ball > table[name][0]:
            table[name][0] = ball
            table[name][1] = time
    else:
        table[name] = [ball, time]
scores = list(table.items())

scores.sort(key=score, reverse=True)
print('\nИтоги соревнований:')
for winner in range(3):
    print(f' {winner + 1} место {scores[winner][0]} ', end=' ')
    print(f'({scores[winner][1][0]})')
