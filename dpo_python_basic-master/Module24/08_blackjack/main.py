import random

class PlayerCard:
    def __init__(self, cost_card, name_card):
        self.cost_card = cost_card
        self.name_card = name_card


class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points


class Game:
    sum_points = 0

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def game_process(self, card_1, card_2):
        if self.sum_points >= 21:
            play_card_14.cost_card = 1
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            print(self.player_1.points, card_1.name_card)
        else:
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            self.sum_points = (self.player_1.points + self.player_2.points)
            print('Очки:', self.player_1.points, ' добрали: ', card_1.name_card)

    def winner(self):
        if self.player_1.points > 21 and self.player_2.points > 21:
            print('Нет победителей. У обоих игроков перебор.')
            print(f'{self.player_1.name}, набрал {self.player_1.points} очков. {self.player_2.name} набрал {self.player_2.points} очков.')
        elif self.player_1.points > 21:
            print(f' Победил {self.player_2.name}, набрав {self.player_2.points} очков. У {self.player_1.name} перебор {self.player_1.points} очков.')
        elif self.player_2.points > 21:
            print(f' Победил {self.player_1.name}, набрав {self.player_1.points} очков. У {self.player_2.name} перебор {self.player_2.points} очков.')
        elif self.player_1.points == self.player_2.points:
            print(f' Ничья! У обоих игроков {self.player_1.points} очков.')
        elif self.player_1.points > self.player_2.points:
            print(f' Победил {self.player_1.name}, набрав {self.player_1.points} очков, против {self.player_2.points}.')
        elif self.player_2.points > self.player_1.points:
            print(f' Победил {self.player_2.name}, набрав {self.player_2.points} очков, против {self.player_1.points}.')
        else:
            print('Нет победителей.')


play_card_2 = PlayerCard(2, 'Двойка')
play_card_3 = PlayerCard(3, 'Тройка')
play_card_4 = PlayerCard(4, 'Четвёрка')
play_card_5 = PlayerCard(5, 'Пятёрка')
play_card_6 = PlayerCard(6, 'Шестёрка')
play_card_7 = PlayerCard(7, 'Семёрка')
play_card_8 = PlayerCard(8, 'Восьмёрка')
play_card_9 = PlayerCard(9, 'Девятка')
play_card_10 = PlayerCard(10, 'Десятка')
play_card_11 = PlayerCard(10, 'Валет')
play_card_12 = PlayerCard(10, 'Дама')
play_card_13 = PlayerCard(10, 'Король')
play_card_14 = PlayerCard(11, 'Туз')

desc = [play_card_2, play_card_3, play_card_4, play_card_5, play_card_6, play_card_7, play_card_8,
        play_card_9, play_card_10, play_card_11, play_card_12, play_card_13, play_card_14]

player_1 = Player('Игрок 1')
player_2 = Player('Компьютер')
game = Game(player_1, player_2)

for _ in range(2):
    r_1 = random.choice(range(0, 12))
    r_2 = random.choice(range(0, 12))
    game.game_process(desc[r_1], desc[r_2])

while True:
    r_1 = random.randint(0, 12)
    r_2 = random.randint(0, 12)
    ans = int(input('Введите 1 - чтобы взять ещё карту, 2 - чтобы остановиться: '))
    if ans == 1:
        game.game_process(desc[r_1], desc[r_2])
    else:
        break
    if player_1.points > 21 or player_2.points > 21:
        break

game.winner()

