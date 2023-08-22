from typing import Callable


def counter(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f'{func.__name__} была вызвана: {wrapper.count} раз(а)')
        return res

    wrapper.count = 0
    return wrapper


@counter
def fun_1() -> None:
    x = 1+1


@counter
def fun_2() -> None:
    x = 2+2


fun_1()
fun_1()
fun_2()
fun_1()
fun_1()
