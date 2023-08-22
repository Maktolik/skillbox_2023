family_dict = {
('Сидоров', 'Никита'): 35,
('Сидорова', 'Алина'): 34,
('Сидоров', 'Павел'): 10,
('Иванов', 'Павел'): 45,
('Иванова', 'Лена'): 41,
('Корина', 'Влада'): 16
}


surname = input("Введите фамилию: ").lower()
if surname[-1] == 'а':
    sur_man = surname[:-1]
    for i_name, i_age in family_dict.items():
        if i_name[0].lower() == surname or i_name[0].lower() == sur_man:
            print(i_name[0], i_name[1], i_age)
else:
    sur_woman = surname + 'а'
    for i_name, i_age in family_dict.items():
        if i_name[0].lower() == surname or i_name[0].lower() == sur_woman:
            print(i_name[0], i_name[1], i_age)