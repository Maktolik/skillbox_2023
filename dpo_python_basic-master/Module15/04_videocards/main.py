def main():
    nvidea = [3070, 2060, 3090, 3070, 3090]
    for i in range(0, len(nvidea)):
        print(f'{i + 1} Видеокарта:')
    print('Старый список видеокарт:', nvidea)
    max_num = max(nvidea)
    stock = []
    for ind in range(0, len(nvidea)):
        if nvidea[ind] != max_num:
            stock.append(nvidea[ind])
    print('Новый список видеокарт: ', stock)


main()



