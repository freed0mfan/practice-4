name = input('Здравствуйте! Как Вас зовут? ')
print(f'Очень приятно, {name}! Меня зовут Марк.')
age = int(input('Сколько Вам лет? '))

if 78 > age:
    print(f'Да, {name}, я старше Вас на {78-age} лет.')
elif age == 78:
    print(f'{name}, мы с Вами одного возраста!')
else:
    print(f'Да, {name}, Вы старше меня на {age-78} лет.')

programmer = input('Вам нравится программировать? ')

if programmer.casefold() == 'да':
    print('Превосходно! Уверен, вы преуспеете в этом.')
elif programmer.casefold() == 'нет':
    print('Жаль. Я думал, вы сможете написать интересную программу для меня.')

