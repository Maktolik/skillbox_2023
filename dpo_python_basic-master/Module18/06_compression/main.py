def main():
    txt = input('Введите строку: ')
    str_len = len(txt)
    res = ''

    if str_len > 0:
        i = 0
        while i < str_len:
            count = 0
            char = txt[i:i + 1]
            while i < str_len and txt[i] == char:
                i += 1
                count += 1
            res += char + str(count)
        print(res)

main()