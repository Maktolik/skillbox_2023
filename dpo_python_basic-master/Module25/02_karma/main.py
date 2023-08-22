import random


class Buddist:
    """
    Базовый класс , описывающий  Буддиста
    Args:
    karma(int): значение кармы (0 начальное)
    """
    def __init__(self, karma: int ):
        self.karma = karma

    def get_karma(self) -> int:
        """
        геттер кармы
        :return: karma(int)
        """
        return self.karma

    def set_karma(self, karma: int):
        """
        Сеттер кармы
        прибавялет карму (int)
        """
        self.karma += karma

"""Классы для выкидывания нужных ошибок"""
class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    """
    Основная функция, определяет прибавку к карме (1-7) или выврос исключения (1 к 10)
    :return: randint(1,7): int
    """
    if random.randint(1, 10) == 1:
        raise random.choice([KillError('Убийство'),
                             DrunkError('Напился'),
                             CarCrashError('Разбил машину'),
                             GluttonyError('Чревоугодие'),
                             DepressionError('Депрессия')])
    else:
        return random.randint(1, 7)


buddist = Buddist(0)
day = 0
while buddist.get_karma() < 500:
    """
    Основной цикл для решения
    пока не набралось 500 кармы, 
    считает дни в day (int)
    добавляет карму в res(int)
    при выявлении исключения, записывает его в файл karma.log
    """
    day += 1
    try:
        res = one_day()
        buddist.set_karma(res)
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as err:
        with open('karma.log', 'a', encoding='utf8') as karma_log:
            karma_log.write(f'День {day}: Проступок: {err}\n')
