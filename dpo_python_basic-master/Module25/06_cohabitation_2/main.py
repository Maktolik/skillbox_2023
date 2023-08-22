import random


class Home:
    """
    базовый класс Дом
    Attributes:
        money:int: def=100 деньги семьи
        food:int: def=50 еда в доме
        cat_food:int: def=30 еда кота
        dirt:int: def=0 уровеьн грязи

    выводит аттрибуты:str

    """
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0

    def act(self, family):
        """метод описывает действия каждого в family"""
        for i in family:
            i.act()
            if self.dirt > 90 and not isinstance(i, Cat):
                i.happiness -= 10
            if i.satiety < 0:
                raise Warning(f'{i.name} погиб от голода!')
            elif not isinstance(i, Cat) and i.happiness < 10:
                raise Warning(f'{i.name} погиб от депрессии')
            print(i)
            print(self)

    def __str__(self):
        return f'Деньги: {self.money}, Еда: {self.food}, Еда кота: {self.cat_food}, Грязь: {self.dirt}\n'


class Family:
    """
    Класс семья
    Args:
        name:str имя существа
        satiety:int -сытость
        home: -дом

    вывод:str: состояние
    """
    def __init__(self, name, home):
        self.name = name
        self.satiety = 30
        self.home = home

    def eating(self):
        """метод описывает прием пищи"""
        food_amount = random.randrange(10, 30)
        self.satiety += food_amount
        self.home.food -= food_amount
        print(f'{self.name}, ест')

    def act(self):
        """
        метод описывает возможные действия для данного класса
        для всех в семье доступно действие поесть
        """
        if self.satiety < 30 and self.home.food != 0:
            self.eating()

    def __str__(self):
        return f'{self.name}, Сытость {self.satiety}'


class Human(Family):
    """
    класс для только людей, родитель : Family
    Args:
        name:str: имя
        home:str: дом
        happiness:int: уровень счастья
    """
    def __init__(self, name, home):
        super().__init__(name, home)
        self.happiness = 100

    def pet_cat(self):
        """метод описывает поглаживание кота"""
        self.happiness += 5
        self.satiety -= 10

    def act(self):
        """
        метод описывает возможные действия для данного класса
        для всех в Human доступно действие гладить кота
        +действия класса родителя
        """
        super().act()
        if self.happiness < 20:
            self.pet_cat()


class Husband(Human):
    """
    класс для мужа, родитель: Human
    Args:
        name:str: имя
        home: дом
        happiness:int: уровень счастья
    """

    def playing(self):
        """метод описывает действие играть"""
        self.satiety -= 10
        self.happiness += 20
        print(f'{self.name}, Играет')

    def work(self):
        """метод, описывает действие работа"""
        self.satiety -= 10
        self.home.money += 150
        print(f'{self.name}, Работает')

    def act(self):
        """
        метод описывает возможные действия для данного класса
        для всех в Husband доступно действие работать и играть
        +действия класса родителя
        """
        super().act()
        if self.home.money < 100:
            self.work()
        else:
            self.playing()


class Wife(Human):
    """
    класс жена, родитель: Human
    Args:
        name:str имя существа
        satiety:int -сытость
        home:объект класса -дом

    """
    def buy_food(self):
        """метод описывает покупку еды"""
        self.home.food += 30
        self.home.money -= 40
        self.home.cat_food += 10
        self.satiety -= 10
        print(f'{self.name}, Пошла за покупками')

    def buy_coat(self):
        """метод описывает покупку шубы"""
        self.home.money -= 50
        self.happiness += 60
        self.satiety -= 10
        print(f'{self.name}, Купила шубу')

    def clean_house(self):
        """метод описывает уборку в доме"""
        self.home.dirt -= random.randrange(1, 100)
        self.satiety -= 10
        print(f'{self.name}, Убирает дом')

    def act(self):
        """
        метод описывает возможные действия для данного класса
        для всех в Husband доступно действие уборка, покупка шубы, покупка продуктов
        +действия класса родителя
        """
        super().act()
        if self.home.food < 30 or self.home.cat_food < 30:
            self.buy_food()
        elif self.home.dirt > 60:
            self.clean_house()
        else:
            self.buy_coat()


class Cat(Family):
    """
    Класс кота, родитель : Family
    Args:
        name:str: имя
        home: дом
    """

    def eating(self):
        """метод описывает употредление кошачьей еды"""
        if self.home.cat_food <= 30:
            food_amount = random.randrange(10, self.home.cat_food)
        else:
            food_amount = random.randrange(10, 30)
        self.home.cat_food -= food_amount
        self.satiety += 2 * food_amount

    def tear_wallpaper(self):
        """метод описывает обдирание обоев"""
        self.home.dirt += 5
        self.satiety -= 10
        print(f'{self.name}, Дерёт обои')

    def act(self):
        """
        метод описывает возможные действия для данного класса
        для всех в Cat доступно обдирание обоев
        +действия класса родителя
        """
        super().act()
        self.tear_wallpaper()


home = Home()

husband = Husband('Миша', home)
wife = Wife('Лена', home)
cat = Cat('Жорик', home)
family_list = [husband, wife, cat]
for day in range(1, 366):
    print('День,', day)
    home.act(family_list)