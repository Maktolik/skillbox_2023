import math
import random


class Car:
    """
    базовый класс машины
    Args:
        x,t : int - координаты транспорта
        fi:float - угол

    :return:str координаты х, у

    """
    def __init__(self, x: int, y: int, fi: float):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist: float):
        """метод реализует движение, изменяя координаты х,у"""
        self.x = self.x + dist * math.cos(self.fi)
        self.y = self.y + dist * math.sin(self.fi)

    def __str__(self):
        return f'Координаты: X={round(self.x, 2)} Y={round(self.y, 2)}'


class Bus(Car):
    """
    класс автобус, родитель: Car
    Args:
        x,t : int - координаты транспорта
        dir:float - напр движения
        passengers: int - количество пассажиров
        money:float - заработано денег


    :return:str координаты х, у, колличество пассажиров, заработанные деньги

    """
    def __init__(self, x: int, y: int, dir: float):
        super().__init__(x, y, dir)
        self.passengers = 0
        self.money = 0

    def move(self, dist: float):
        """
        наследует метод движения класса родителя+
        расчитывает заработанные деньги от пройденного расстояния
        """
        self.money += self.passengers * dist
        super().move(dist)

    def enter(self, passengers: int):
        """метод реализует вход пассажиров (int) 0, 1 ,2 человека"""
        self.passengers += passengers

    def exit(self, passengers: int):
        """метод реализует выход пассажиров (int) 0, 1 ,2 человека"""
        if passengers > self.passengers:
            self.passengers = 0
        else:
            self.passengers -= passengers

    def __str__(self):
        info = [
            super().__str__(),
            f'В автобусе {self.passengers} пассажиров.',
            f'Заработано {round(self.money, 3)} рублей.',
        ]
        return '\n'.join(info)


def main():
    """
    основная функция, создает экземпляры классов Car и Bus
    симулирует 10 случайных действий входа-выхода пассажиров
    :print: str Car и Bus
    """
    car = Car(0, 0, 90)
    bus = Bus(2, 2, 50)

    for _ in range(10):
        car.move(random.randint(0, 360))
        print(car)
        pas_action = random.randint(1, 2)
        if pas_action == 1:
            if bus.passengers > 0:
                bus.exit(random.randint(0, 2))
            else:
                bus.enter(random.randint(0, 2))
        bus.move(random.randint(0, 360))
        print(bus)

main()
