def interests_len(data):
    interests = []
    surnames = ''
    for i in data:
        interests += (data[i]['interests'])
        surnames += data[i]['surname']
    interests.sort()
    return interests, len(surnames)


def main():
    students = {
        1: {
            'name': 'Bob',
            'surname': 'Vazovski',
            'age': 23,
            'interests': ['biology', 'swimming']
        },
        2: {
            'name': 'Rob',
            'surname': 'Stepanov',
            'age': 24,
            'interests': ['math', 'computer games', 'running']
        },
        3: {
            'name': 'Alexander',
            'surname': 'Krug',
            'age': 22,
            'interests': ['languages', 'health food']
        }
    }

    pairs = [(i, students[i]['age']) for i in students]
    print('Список пар "ID студента - Возраст":', pairs)

    int_sur_len = interests_len(students)
    print('Полный список интересов всех студентов:', int_sur_len[0])
    print('Общая длина всех фамилий студентов:', int_sur_len[1])


main()
