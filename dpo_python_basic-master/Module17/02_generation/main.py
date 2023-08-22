def main():
    number = int(input('Введите длину списка: '))

    res_list = [(1 if x % 2 == 0 else x % 5) for x in range(number)]

    print(res_list)

main()