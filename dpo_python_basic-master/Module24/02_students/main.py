class Student:

    def __init__(self, full_name: str, group_number: str, progress: tuple):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def give_avrg(self) -> float:
        return round(sum(self.progress) / len(self.progress), 3)

    def __str__(self):
        return f'ФИ: {self.full_name} - № группы: {self.group_number} - Средний балл: {self.give_avrg()}'


def rec_data():
    name = input('Фамилия Имя: ')
    group = input('Номер группы: ')
    marks = tuple(map(int, input('Оценки: ').split()))
    return name, group, marks


lst_student = [Student(*rec_data()) for i in range(2)]
print('Список студентов:')
for student in lst_student:
    print(student)
print()

lst_student.sort(key=lambda avg: avg.give_avrg())
print('Список студентов отсортированный:')
for student in lst_student:
    print(student)
