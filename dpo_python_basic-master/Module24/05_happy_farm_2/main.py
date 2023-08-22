class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def collect(self):
        if self.state != 0:
            self.state = 0
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def collect_all(self):
        print('Картошка собрана!')
        for i_potato in self.potatoes:
            i_potato.collect()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')


class Gardener:
    def __init__(self, name: str, garden: PotatoGarden):
        self.name = name
        self.garden = garden

    def care(self):
        self.garden.grow_all()

    def gather(self):
        self.garden.collect_all()


new_garden = PotatoGarden(5)
man_1 = Gardener('Садовник', new_garden)
man_1.care()
man_1.care()
man_1.care()
man_1.gather()