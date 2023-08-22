numbers = int(input('Введите максимальное число: '))
nums = set(range(1, numbers + 1))
while True:
    ans = input('Нужное число есть среди вот этих чисел: ')
    if ans == 'Помогите!':
        break
    ans = {int(i) for i in ans.split()}
    artem = input('Ответ Артёма: ')
    if artem == 'Да':
        nums &= ans
    else:
        nums -= ans

print(f'Артём мог загадать следующие числа: {nums}')