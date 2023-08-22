class Parent:
    childrens = []

    def __init__(self, name: str, age: int, childrens):
        self.name = name
        self.age = age
        for child in childrens:
            if age - child.age > 16:
                self.childrens.append(child)

    def __str__(self):
        return self.name + ' ' + str(self.age) + '\n' + '\n'.join(str(child) for child in self.childrens)

    def calming(self, children):
        for child in self.childrens:
            if child is children:
                child.calm = True

    def is_hunger(self, children):
        for child in self.childrens:
            if child is children:
                child.hunger = True


class Children:

    def __init__(self, name: str, age: int, calm: bool, hunger: bool):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger

    def __str__(self):
        calm_is = ('Спокоен' if self.calm else 'Плачет')
        hunger_is = ('Покушал' if self.hunger else 'Голоден')
        return (f'{self.name} {self.age} лет {calm_is} {hunger_is}')


ch_1 = Children('Катя', 1, False, False)
ch_2 = Children('Женя', 13, True, False)
ch_3 = Children('Рома', 20, True, True)
pr_1 = Parent('Лена', 54, [ch_1, ch_2, ch_3])
print(pr_1)
pr_1.calming(ch_1)
pr_1.is_hunger(ch_2)
print(pr_1)
