ip = input('Введите IP: ').split('.')

if len(ip) < 4:
    print('Адрес - это четыре числа, разделённые точками')
else:
    num = 0
    out_range = 0
    for x in ip:
        if x.isdigit():
            num += 1
            if int(x) > 255:
                out_range += 1
                print(x, 'превышает 255')
        else:
            print(x, '- не целое число')
    if out_range == 0 and num == 4:
        print('IP-адрес корректен')