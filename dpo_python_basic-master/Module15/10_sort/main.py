def sort(lists):
    for element in range(len(lists) - 1):
        for i in range(len(lists) - 1 - element):
            if lists[i] > lists[i + 1]:
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
    return lists


def main():
    lists = [1, 4, -3, 0, 10]
    print('Изначальный список:', lists)
    lists_new = sort(lists)
    print('Отсортированный список:', lists_new)


main()

