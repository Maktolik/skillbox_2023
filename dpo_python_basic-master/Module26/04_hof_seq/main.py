class QHofstadter:
    def __init__(self, sequence: list):
        self.sequence = sequence[:]
        if sequence != [1, 1]:
            raise ValueError('Не верно указано число последовательностей.')
        if self.sequence[0] != self.sequence[1]:
            raise ValueError('Значения последовательности не совпадают.')

    def __str__(self) -> str:
        return ', '.join(str(elem) for elem in self.sequence)

    def __next__(self):
        try:
            q = self.sequence[-self.sequence[-1]] + self.sequence[-self.sequence[-2]]
            self.sequence.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.sequence


q1 = QHofstadter([1, 1])
next(q1)
next(q1)
next(q1)

print(q1)

# q2 = QHofstadter([1, 2])
# next(q2)
# print(q2)
