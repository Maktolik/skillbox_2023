import math
def check_coord(x, y, r):
    return math.sqrt(x * x + y * y) <= r

def main():
    print('Введите координаты монетки:')
    x = float(input('X: '))
    y = float(input('Y: '))
    rad = int(input('Введите радиус: '))

    if check_coord(x, y, rad):
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')

main()