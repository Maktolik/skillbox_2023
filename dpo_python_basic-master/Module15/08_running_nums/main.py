def main():
    lists = [1, 2, 3, 4, 5]
    new_lists = []
    K = 6
    swap = int(K % len(lists))
    for i in range(len(lists)):
        new_lists.append(lists[i - swap])
    print('Изначальный список:', lists)
    print('Передвинутый список:', new_lists)


main()

