import time
import random
from typing import Callable


def slow(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(random.randint(1,15))
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения: {end - start} секунд.')
        return res

    return wrapper


@slow
def get_page(page: str) -> str:
    print(f'Получение данных со страницы: {page}')


page = get_page('https://google.com')