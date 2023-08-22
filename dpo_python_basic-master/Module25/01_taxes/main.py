class Property:
    """
    Базовый класс , описывающий  Property

    Args:
        worth(float): стоимость
    """
    def __init__(self, worth: float) -> None:
        self.__worth = worth

    @property
    def worth(self) -> float:
        """
        Геттер стоимости

        :return: __worth
        :rtype: float
        """

        return self.__worth

    @worth.setter
    def worth(self, worth: float) -> None:
        """
        Сеттер стоимости

        :param worth: стоимость
        :type worth float
        """
        self.__worth = worth

    def tax(self):
        """
        Используется в дочерних классах
        """
        pass


class Apartment(Property):
    """
    Класс Apartment, родитель: Property

    Args:
        worth(float): стоимость
    """

    def tax(self) -> float:
        """
        Вывод расчетного налога для класса Apartment (1/1000)

        :return: self.worth / 1000
        :rtype: float
        """
        return self.worth/1000


class Car(Property):
    """
    Класс Car, родитель: Property

    Args:
    worth(float): стоимость
    """
    def tax(self) -> float:
        """
        Вывод расчетного налога для класса Car (1/200)

        :return: self.worth / 200
        :rtype: float
        """
        return self.worth / 200


class CountryHouse(Property):
    """
    Класс CoubtryHouse, родитель: Property

    Args:
    worth(float): стоимость
    """

    def tax(self) -> float:
        """
        Вывод расчетного налога для класса Car (1/500)

        :return: self.worth / 500
        :rtype: float
        """
        return self.worth / 500


def main():
    """
    Основная функция
    Вначале цикл для входных атрибутов:
    Attributes:
    cash:float:  переменная для хранения имеющихся средств
    worth:float: переменная для хранения  стоимости имущества
    answer:int: переменная для проверки выбора действия
    В try задается выбор с имуществом ( 1 2 3 ) , и выбор (0) для выхода из цикла, при верных данных программа считает дальше,
    ичане в exept обработка иного выбора (не 1 2 3 0), при котором идет повторный ввод данных и answer.
    
    после выхода из цикла
    создается экземлряр, в зависимости от выбора и
    идет расчет налога obj.tax:float , затем количество недостающих средств need_money:float

    """


while True:
    try:
        cash = float(input('Имеется средств: '))
        worth = float(input('Стоимость имущества: '))
        answer = int(input(' Имущество \n' +
                               ' 1 - Дом\n' +
                               ' 2 - Автомобиль\n' +
                               ' 3 - Дача\n' +
                               ' 0 - Выход\n'))
        if answer not in (1, 2, 3, 0):
            raise ValueError
        else: break
    except ValueError:
        print('Ошибка. Попробуйте ещё раз.\n')

if answer == 1:
    obj = Apartment(worth)
elif answer == 2:
    obj = Car(worth)
elif answer == 3:
    obj = CountryHouse(worth)
if cash > (worth - obj.tax()):
    need_money = -1
else:
    need_money = (worth - obj.tax()) - cash
print('\nНалог:', obj.tax())
if need_money == -1:
    print('У Вас хватает денег!\n')
else:
    print(f'Необходимо ещё денег: {str(need_money)}')

main()
