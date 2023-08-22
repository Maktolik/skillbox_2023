from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


floats_1 = list(map(lambda x: round(x ** 3, 3), floats))
print(floats_1)

names_2 = list(filter(lambda x: len(set(x)) >= 5, names))
print(names_2)

numbers_3 = reduce(lambda prev, cur: prev * cur, numbers)
print(numbers_3)
