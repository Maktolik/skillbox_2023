list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
desired = 56


def iter_list(list_one: list, list_two: list, search: int):
    for num in list_one:
        for y in list_two:
            result = num * y
            print(num, y, result)
            if result == search:
                yield True
            yield False


finding = iter_list(list_1, list_2, desired)

for i in finding:
    if next(finding):
        print(f'{desired} найдено!!')
        finding.close()