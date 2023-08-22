def main():

        shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
                ['педаль', 100], ['седло', 1500], ['рама', 12000],
                ['обод', 2000], ['шатун', 200], ['седло', 2700]]
        det_count = 0
        det_cost = 0
        det = input('Название детали: ')

        for i in range(len(shop)):
                if shop[i][0] == det:
                        det_count += 1
                        det_cost += shop[i][1]
        print()
        if det_count > 0:
                print('Кол-во деталей -', det_count)
                print('Общая стоимость -', det_cost)
        else:
                print('Товар не найден.')

main()