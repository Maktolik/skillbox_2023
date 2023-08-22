class Stack:
    """
    класс стек
    Args:
        __list:list- список задач
    """
    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(", ".join(self.__list))

    def add(self, elem):
        """метод добавляет задачу(elem:str) в лист задач __list"""
        self.__list.append(elem)

    def pop(self):
        """метод удаляет последнюю задачу из листа __list"""
        if len(self.__list) == 0:
            return None
        return self.__list.pop()


class TaskManager:
    """
    класс менеджера задач
    Atributes:
        task: dict: словарь из задач

    выводит отсортированный по ключам (номерам) список задач
    """
    def __init__(self):
        self.task = {}

    def __str__(self):
        string = ""
        for elem in sorted(self.task.keys()):
            string += str(elem) + " " + str(self.task[elem]) + ";\n"
        return string

    def new_task(self, task, priority):
        """
        метод добавление задачи в меннеджер
        Args:
            task:str- задача
            priority:int- приоритет задачи
        """
        if not priority in self.task.keys():
            self.task[priority] = Stack()
            self.task[priority].add(task)
        else:
            new_stack = Stack()
            while len(str(self.task[priority])) != 0:
                value = self.task[priority].pop()
                if value != task:
                    new_stack.add(value)
            new_stack.add(task)
            self.task[priority] = new_stack

    def delete_task(self, priority):
        """
        метод удаления задачи в меннеджере
        Args:
            priority:int- приоритет задачи
        """
        if not priority in self.task.keys():
            print(f'Задача с приоритетом {priority} сейчас нет.')
        else:
            print(f'Удалили задачу {self.task[priority].pop()}')
            if len(str(self.task[priority])) == 0:
                self.task.pop(priority)


manager = TaskManager()
manager.new_task('сделать уборку', 4)
manager.new_task('помыть посуду', 4)
manager.new_task('отдохнуть', 1)
manager.new_task('поесть', 2)
manager.new_task('сдать дз', 2)
print(manager)
# manager.new_task('сделать уборку', 4)
manager.delete_task(2)
manager.delete_task(2)
manager.delete_task(2)
# manager.delete_task(1)
print(manager)
