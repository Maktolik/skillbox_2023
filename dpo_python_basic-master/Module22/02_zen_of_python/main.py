file = open('zen.txt', 'r')
to_rev = file.readlines()
to_rev.reverse()
print(''.join(to_rev))