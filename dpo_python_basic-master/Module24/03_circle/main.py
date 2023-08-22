class Circle:
    pi = 3.14159

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_sq(self) -> float:
        return self.r * self.r * self.pi

    def get_per(self) -> float:
        return 2 * self.r * self.pi

    def scale(self, k: float):
        self.r *= k

    def intersection(self, outsider):
        return (self.x - outsider.x) ** 2 + (self.y - outsider.y) ** 2 <= (self.r + outsider.r) ** 2


print('Окружность 1')
c_1 = Circle(2, 2, 2)
print(f'Площадь первого круга {c_1.get_sq()}')
print(f'Периметр первого круга{c_1.get_per()}')
c_1.scale(2)
print(f'Площадь первого круга после увеличения {c_1.get_sq()}')
print(f'Периметр первого круга после увеличения {c_1.get_per()}')

print('\nОкружность 2')
c_2 = Circle(3, 3, 3)
print(f'Площадь второго круга {c_2.get_sq()}')
print(f'Периметр второго круга {c_2.get_per()}')
c_2.scale(2)
print(f'Площадь второго круга после увеличения {c_2.get_sq()}')
print(f'Периметр второго круга после увеличения {c_2.get_per()}')

print('\nПересекаются ли круги?:')
print(c_1.intersection(c_2))