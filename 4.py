print('Вы поедете на бал?')
ans = input('Ответ: ')
forbdn = ['да', 'нет']

if ans.casefold() not in forbdn:
    print('Верно')
else:
    print('Неверно')
