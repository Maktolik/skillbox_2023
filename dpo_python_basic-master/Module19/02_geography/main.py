data = {}
country = int(input('Кол-во стран: '))

for i in range(country):
    value = input(f'{i + 1} страна: ').split()
    for city in value[:]:
        data[city] = value[0]

for i in range(3):
    city = input(f'\n{i + 1} город: ')
    country = data.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')
