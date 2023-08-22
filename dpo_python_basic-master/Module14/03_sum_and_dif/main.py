def summ_fig(num):
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    return sum
def count_fig(num):
    count = 0
    while (num != 0):
        count += 1
        num = num // 10
    return count

def main():
    num = int(input("Введите целое число: "))
    summ = summ_fig(num)
    print(f'Сумма чисел: {summ}')
    count = count_fig(num)
    print(f'Количество цифр: {count}')
    print(f'Разность суммы и количества цифр: {summ-count}')

main()

