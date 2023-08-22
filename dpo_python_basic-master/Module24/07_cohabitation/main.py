import random

class Person:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.health = 50

    def print_info(self):
        print(f'Имя жильца: {self.name}, Состояние здоровья: {self.health}')

    def spend_day(self):
        if self.health >= 5:
            random_num = random.randint(1, 6)
            if self.health < 20:
                self.eat()
            elif self.house.fridge < 10:
                self.market()
            elif self.house.money < 50 or random_num == 1:
                self.work()
            elif random_num == 2:
                self.eat()
            else:
                self.play()
        else:
            print(f'К сожалению, {self.name} помер с голоду ')
            raise SystemExit

    def eat(self):
        self.health += 1
        self.house.fridge -= 1
        return f'ест, сытость {self.health} еда {self.house.fridge}'

    def work(self):
        self.health -= 1
        self.house.money += 1
        return f'работает, сытость {self.health} деньги {self.house.money}'

    def play(self):
        self.health -= 1
        return f'играет, сытость {self.health}'

    def market(self):
        self.house.fridge += 1
        self.house.money -= 1
        return f'идет в магазин, еда {self.house.fridge} деньги {self.house.money}'


class House:
    def __init__(self, food, money):
        self.fridge = food
        self.money = money
    def print_info(self):
        print(f'Еды в холодильнике - {self.fridge}, денег в тумбочке - {self.money}')


house = House(50, 0)
person = Person("Рома", house)
for _ in range(365):
    person.spend_day()
else:
    print(f"{person.name} выжил!")

house_2 = House(50, 0)
people = Person("Лена", house_2), Person("Женя", house_2)
for _ in range(365):
    for person in people:
        person.spend_day()
else:
    names = (person.name for person in people)
    print(*names, sep=", ", end=" ")
    print("выжили!")
