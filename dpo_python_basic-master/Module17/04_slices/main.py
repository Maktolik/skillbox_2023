def main():
    alphabet = 'abcdefg'

    copy = alphabet
    print('1:', copy)
    print('2:', alphabet[::-1])
    print('3:', alphabet[::2])
    print('4:', alphabet[1::2])
    print('5:', alphabet[:1])
    print('6:', alphabet[len(alphabet) - 1:])
    print('7:', alphabet[int(len(alphabet) / 2):int(len(alphabet) / 2 + 1)])
    print('8:', alphabet[int(len(alphabet) - 3):])
    print('9:', alphabet[3:5])
    print('10:', alphabet[4:2:-1])

main()