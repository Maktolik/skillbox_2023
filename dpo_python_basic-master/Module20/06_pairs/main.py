import random

orig_lst = [random.randint(0, 9) for _ in range(10)]

print('Оригинальный список:', orig_lst)

zip_lst = zip(orig_lst[::2], orig_lst[1::2])
new_lst = []
for i in zip_lst:
    new_lst.append(i)
print('Новый список:', new_lst)