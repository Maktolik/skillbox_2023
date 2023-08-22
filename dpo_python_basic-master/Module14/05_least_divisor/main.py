def get_nd(num):
    nd = 1
    for i in range(1, num + 1):
        if num % i == 0:
            nd = i
        if nd > 1:
            break
    return nd
def main():
    number = int(input('Введите число: '))
    print('Наименьший делитель, отличный от единицы:', get_nd(number))

main()