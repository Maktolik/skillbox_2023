def moves(A, B=1, C=3):
    if A == 1:
        print(f'Переложит диск {A} со стержня номер {B} на стержень номер {C}')
    else:
        moves(A - 1, B, 6 - B - C)
        print(f'Переложит диск {A} со стержня номер {B} на стержень номер {C}')
        moves(A - 1, 6 - B - C, C)


disc = int(input('Введите количество дисков: '))
moves(disc)
