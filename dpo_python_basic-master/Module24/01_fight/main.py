import random

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, enemy):
        if type(self) == type(enemy):
            enemy.health -= 20
        else:
            raise TypeError('Не того атакует')

def main():

    warriors = [Warrior('Воин 1'), Warrior('Воин 2')]

    while True:
        menu = input('Введите А, чтобы начать бой.\nВведите 0, чтобы закончить: ').upper()
        if menu == 'A' or menu == 'А':
            i = random.randint(0, 1)
            attacker, deffender = warriors[i], warriors[i - 1]
            attacker.attack(deffender)
            print(attacker.name, 'атаковал', deffender.name)
            print('У', deffender.name, 'осталось здоровья', deffender.health)
            if deffender.health <= 0:
                print(attacker.name, 'победил!!!')
                break
        elif menu == '0':
            break
        else:
            print('Ошибка ввода. Возврат в главное меню.')
            main()


main()
