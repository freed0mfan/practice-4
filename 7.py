records = input('Рекорды: ')
first = int(records.split(' ')[0])
second = int(records.split(' ')[1])
third = int(records.split(' ')[2])

if first >= second and first >= third:
    print(first)
elif second >= first and second >= third:
    print(second)
else:
    print(third)
