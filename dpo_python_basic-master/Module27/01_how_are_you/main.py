from typing import Callable


def how_are_you(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapper


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def summ(x: int, y: int) -> int:
    result = x + y
    print(f'Сумма {x} и {y} равна {result}')
    return result


@how_are_you
def calc(x: int, y: int) -> int:
    result = x ** y
    print(f'{x} в степени {y} равен {result}')
    return result


test()
summ(1, 313)
calc(2,3)
