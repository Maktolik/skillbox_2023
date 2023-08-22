def print_num(end, start=1):
    if start <= end:
        print(start)
        print_num(end, start + 1)


res = int(input('Введите num: '))
print_num(res)
