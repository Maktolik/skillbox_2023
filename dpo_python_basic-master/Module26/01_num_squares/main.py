from collections.abc import Iterable


class SquaresNumbers:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__first_elem = 0
        self.__counter = 0

    def __iter__(self):
        self.__first_elem = 0
        self.__counter = 0
        return self

    def __next__(self) -> int:
        self.__counter += 1
        if self.__limit <= 0:
            raise StopIteration
        elif self.__limit >= 1:
            if self.__counter > self.__limit:
                raise StopIteration
        self.__first_elem += 1
        return self.__first_elem * self.__first_elem


def squares(nums: int) -> Iterable[int]:
    for num in range(1, nums + 1):
        yield num ** 2


number = int(input('Введите число N: '))
squaresNumbers = SquaresNumbers(limit=number)
print('\nВывод класса-итератора')
for num_i in squaresNumbers:
    print(num_i, end=' ')

print('\nВывод функции-генератора')
for x in squares(number):
    print(x, end=' ')

print('\nВывод генераторного выражения')
squareGen = (num ** 2 for num in range(1, number + 1))
for i_num in squareGen:
    print(i_num, end=' ')
