def check_array(check_list):
    return [i for i, v in enumerate(check_list) if is_prime(i)]


def is_prime(i_num):
    if i_num >= 2:
        result = True
        for i in range(2, i_num):
            if i_num % i == 0:
                result = False
                break
    else:
        result = False
    return result


def crypto(text):
    lst = check_array(text)
    elements = []
    for i in lst:
        elements.append(text[i])
    return elements


print(crypto('О Дивный Новый мир!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
