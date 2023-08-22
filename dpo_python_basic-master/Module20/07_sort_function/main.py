def tpl_sort(tpl):
    for el in tpl:
        if not isinstance(el, int):
            return tpl
    return tuple(sorted(tpl))


print(tpl_sort([6, 3, -1, 8, 4, 10, -5]))
print(tpl_sort([6, 3, -1, 8, 'a', 10, -5]))
