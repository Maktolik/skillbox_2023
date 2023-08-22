class Person:
    """
    базовый класс,определяет члюбого человека,
    Args:
        name:str : имя
        surname:str : фамилия
        age: int : возраст

    Выводит информацию о людях
    """
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'{self.__name} {self.__surname} {self.__age}'


class Employee(Person):
    """
    Класс работников, родитель:Person
    метод возвращает зарплату
    """
    def calc_salary(self):
        pass


class Manager(Employee):
    """
    Класс менеджеров, родитель: Employe
    Args:
        name:str : имя
        surname:str : фамилия
        age: int : возраст

    :return:int: ( 13000 константа)

    """
    __salary = 13000
    def calc_salary(self):
        return self.__salary


class Agent(Employee):
    """
    Класс агентов, родитель: Employee
    Args:
        name:str : имя
        surname:str : фамилия
        age: int : возраст
        sales: int: количество продаж
    :return:float (5000 + 0.05 * продажи )
    """
    def __init__(self, name: str, surname: str, age: int, sales: int):
        super().__init__(name, surname, age)
        self.__sales = sales

    def calc_salary(self):
        return 5000 + 0.05 * self.__sales


class Worker(Employee):
    """
    Класс работников, родитель: Employee
        Args:
            name:str : имя
            surname:str : фамилия
            age: int : возраст
            hours: int: количество отработанных часов
        :return:float (100 * часы)
    """
    def __init__(self, name: str, surname: str, age: int, hour: int):
        super().__init__(name, surname, age)
        self.__hours = hour

    def calc_salary(self):
        return 100 * self.__hours


def main():
    """
    Список из девяти объектов: первые три — Manager, следующие три — Agent и последние три — Worker.
    #возможно вынести доп.аргументы типо продаж и часов из словаря и задавать рандомно при создании экземпляров

    :Print: фамилия имя возраст : зарплата
    """
    employees = list()
    fia = [('Олег', 'Петорв', 25), ('Валера', 'Еров', 24), ('Дмитрий', 'Нагиев', 22),
                ('Игорь', 'Воронин', 21, 10000), ('Лена', 'Иванова', 44, 15000), ('Катя', 'Еремолова', 19, 21212),
                ('Контсантин', 'Мигунов', 44, 12), ('Адольф', 'Михайлов', 33, 13), ('Петр', 'Петров', 42, 10)
                ]
    for i in range(3):
        employees.append(Manager(fia[i][0], fia[i][1], fia[i][2]))
    for i in range(3, 6):
        employees.append(Agent(fia[i][0], fia[i][1], fia[i][2], fia[i][3]))
    for i in range(6, 9):
        employees.append(Worker(fia[i][0], fia[i][1], fia[i][2], fia[i][3]))

    for emp in employees:
        print(emp,'лет, зарплата:', emp.calc_salary())

main()
