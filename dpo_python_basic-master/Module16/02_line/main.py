def main():
    class1 = list(range(160, 177, 2))
    class2 = list(range(162, 181, 3))

    class1.extend(class2)
    for i_cur in range(len(class1) - 1):
        for i in range(len(class1) - 1):
            if class1[i] > class1[i + 1]:
                class1[i], class1[i + 1] = class1[i + 1], class1[i]

    print('Отсортированный список учеников:', class1)

main()
