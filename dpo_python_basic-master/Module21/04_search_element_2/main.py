def find_key(struct, key, max_depth=None, depth=1):
    result = None

    if max_depth and max_depth < depth:
        return result

    if key in struct:
        return struct[key]

    for sub_struct in struct.values():

        if isinstance(sub_struct, dict):

            result = find_key(sub_struct, key, max_depth, depth=depth + 1)

            if result:
                break

    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ')
if answer.lower() == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
else:
    max_depth = None

print('Значение ключа:', find_key(struct=site, max_depth=max_depth, key=key))
