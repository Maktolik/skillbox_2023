class MyDict(dict):
    """
    Класс MyDict , родитель : dicr

    Args:
        key - ключ,
    :return:
    возвращает существующий ключ, если такого нет, то возвращает 0
    """
    def get(self, key, default = 0):
        return super().get(key, 0)


my_dict = MyDict({'Раз': 1, 'Два': 2, 'Три': 3, 'Четыре': 4})
print('Key 1:', my_dict.get('Раз'))
print('Key 2:', my_dict.get('Два'))
print('Key 3:', my_dict.get('Три'))
print('Key 4:', my_dict.get('Четыре'))
print('Key 5:', my_dict.get('Пять'))
print('Key 6:', my_dict.get('Шесть'))
