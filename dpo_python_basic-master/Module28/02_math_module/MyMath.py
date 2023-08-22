import math
from abc import ABC


class MyMath(ABC):
    """Абстрактный класс MyMath"""

    @classmethod
    def circle_len(cls, radius: int) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_value(cls, edge: int) -> float:
        return edge ** 3

    @classmethod
    def sphere_sq(cls, radius: int) -> float:
        return 4 * math.pi * radius ** 2