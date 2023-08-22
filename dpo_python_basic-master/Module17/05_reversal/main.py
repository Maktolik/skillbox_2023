def main():
    text = input('Введите строку: ')

    char_ind = [ind for ind, char in enumerate(text) if char == 'h']
    start = char_ind[0]
    end = char_ind[len(char_ind) - 1] - 1

    print('Развернутая последовательность между первым и последним h:', text[end:start:-1])

main()