def flating(lst):
    res = []
    for el in lst:
        if isinstance(el, int):
            res.append(el)
        else:
            res.extend(flating(el))
    return res


def summ(*args):
    return sum(flating(args))


res = summ([[1, 2, [3]], [1], 3])
print('Ответ:', res)
res2 = summ(1, 2, 3, 4, 5)
print('Ответ:', res2)
