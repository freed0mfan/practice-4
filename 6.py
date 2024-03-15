score = input('Счет: ')
first = int(score.split(':')[0])
second = int(score.split(':')[1])

if first > second:
    print(1)
elif first == second:
    print(0)
else:
    print(2)
