from functools import wraps
from typing import Callable, Optional, Any


def decorator_with_args_for_any_decorator(enhance_func: Callable) -> Callable:
    def decor(*args, **kwargs) -> Callable:
        def wrapper(func: Callable) -> Callable:
            return enhance_func(func, *args, **kwargs)

        return wrapper

    return decor


@decorator_with_args_for_any_decorator
def decor_decorator(func: Callable, *args, **kwargs) -> Callable:
    @wraps(func)
    def wrapper(func_args: Optional[Any], func_kwargs: Optional[Any]) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        res = func(func_args, func_kwargs)
        return res

    return wrapper


@decor_decorator(100, 'рублей', 200, 'друзей')
def decor_function(text: str, num: int) -> None:
    print("Привет", text, num)


decor_function("Юзер", 101)
