import re

number_lst = ['А578ВЕ777', 'ОР233787', 'К901МН666', 'СТ46599', 'СНИ2929П777', '666АМР666']
privat_num = []
taxi_num = []


def determine(number: str) -> None:
    global privat_num, taxi_num
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', number):
        privat_num.append(number)
    elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', number):
        taxi_num.append(number)


if __name__ == '__main__':
    for item in number_lst:
        determine(item)

    if len(privat_num) > 0:
        print('Список номеров частных автомобилей:', privat_num)
    if len(taxi_num) > 0:
        print('Список номеров такси:', taxi_num)