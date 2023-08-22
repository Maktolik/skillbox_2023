from datetime import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    def wrapper():
        try:
            print(f'{func.__name__} - {func.__doc__}')
            func()
        except Exception as e:
            e = f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {func.__name__} - {e}'
            with open('function_error.log', 'a+', encoding='utf-8') as f:
                f.write(e)
            print(e)

    return wrapper


@logging
def summ() -> None:
    """сумма чисел"""
    x = 1 + 2


@logging
def divis() -> None:
    """деление чисел"""
    x = 2 / 0


@logging
def stringing() -> None:
    """запись строки в переменную"""
    x = 'Записано!'


summ()
divis()
stringing()
