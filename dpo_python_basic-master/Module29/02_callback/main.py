from functools import wraps
from typing import Callable, Dict

app: Dict[str, Callable] = dict()


def callback(route: str) -> Callable:
    """Декоратор колбек функции"""

    def decor_callback(func: Callable) -> Callable:
        app[route] = func

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decor_callback


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера.')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
