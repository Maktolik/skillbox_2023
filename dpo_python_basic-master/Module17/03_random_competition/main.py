import random


def gen_list(size):
    lst = [round(random.uniform(5, 10), 2) for x in range(size)]
    return lst

def main():
    members_in_team = 20

    team_one = gen_list(members_in_team)
    team_two = gen_list(members_in_team)
    winners = [(team_one[i] if team_one[i] > team_two[i] else team_two[i]) for i in range(members_in_team)]

    print('Первая команда:', team_one)
    print('Вторая команда:', team_two)
    print('Победители тура:', winners)

main()