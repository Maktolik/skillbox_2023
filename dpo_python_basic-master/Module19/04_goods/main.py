goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for prod_name, prod_code in goods.items():
    total_quantity = 0
    total_cost = 0
    for prod in store[prod_code]:
        quantity = prod['quantity']
        cost = prod['price']
        total_cost += quantity * cost
        total_quantity += quantity
    print(f'{prod_name,} - {total_quantity} шт, общая стоимость {total_cost} рублей')
