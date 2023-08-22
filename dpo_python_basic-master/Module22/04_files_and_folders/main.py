import os


def file_sizes(path):
    stat = [0, 0, 0]

    for i in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i))):
            file_path = os.path.abspath(os.path.join(path, i))
            file_size = os.path.getsize(file_path)
            stat[0] += file_size
            stat[1] += 1
        else:
            res = file_sizes(os.path.abspath(os.path.join(path, i)))
            stat[0] += res[0]
            stat[1] += res[1]
            stat[2] += 1
    return stat

path = os.path.abspath(os.path.join('..', '..', 'module22'))

res = file_sizes(path)
print(path)
print(f'Размер каталога (в Кб): {round(res[0] / 1024, 2):,}'.replace(',', ' '))
print(f'Количество файлов: {res[1]:,}'.replace(',', ' '))
print(f'Количество подкаталогов: {res[2]:,}'.replace(',', ' '))