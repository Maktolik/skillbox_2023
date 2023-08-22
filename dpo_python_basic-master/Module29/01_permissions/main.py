from functools import wraps
from typing import Callable


def check_permission(user_name: str) -> Callable:
    """
    Декоратор для проверки прав пользователя.
    Возвращает право доступа к функции
    """
    user_permissions = ['admin']

    def check_user_permission(func: Callable) -> Callable:
        @wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            try:
                if user_name in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'У пользователя недостаточно прав для выполнения функцию {func.__name__}')

        return wrapped

    return check_user_permission


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
