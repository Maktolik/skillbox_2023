def zip_analog(*args):
    min_len = min(map(len, args))
    args_tpl = (tuple(el[i] for el in args) for i in range(min_len))
    return args_tpl

def main():
    a = [{'x': 123}, 'baa', 'zxx', '123', 123]
    b = (13, {233, 'yxy'}, [313], 'zcx')
    res = zip_analog(a,b)
    print(*res)

main()

