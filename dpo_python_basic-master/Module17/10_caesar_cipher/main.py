def get_index(symbol, tab, alf):
    index = alf.index(symbol)
    if index + tab > len(alf) - 1:
        index = index + tab - len(alf)
    else:
        index += tab
    return index
def main():

    text = input('Введите сообщение: ').lower()
    tab = int(input('Введите сдвиг: '))

    alf = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    res = ''

    for symbol in text:
        if symbol in alf:
            res += alf[get_index(symbol, tab, alf)]
        else:
            res += symbol

    print(res)

main()