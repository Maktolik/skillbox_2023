site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site

    for in_struct in struct.values():
        if isinstance(in_struct, dict):
            res = find_key(in_struct, key, meaning)
            if res:
                return site



num_sites = int(input('Сколько сайтов: '))
for num in range(num_sites):
    prod_name = input('Введите название продукта для нового сайта: ')
    key = {'title': f'Куплю/продам {prod_name} недорого', 'h2': f'У нас самая низкая цена на {prod_name}'}
    for i in key:
        find_key(site, i, key[i])

    print(f'Сайт для {prod_name}:')
    print(site, '\n')