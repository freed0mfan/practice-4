y = 'да'
n = 'нет'

shorthair = input('Cобака короткошерстной породы? ').casefold()
height_50 = input('Рост собаки менее 50 см? ').casefold()
if shorthair == y and height_50 == y:
    tail = input('У собаки короткий хвост? ').casefold()
    if tail == y:
        print('английский бульдог')
    elif tail == n:
        ears = input('У собаки длинные уши? ').casefold()
        if ears == y:
            print('гончая')
        elif ears == n:
            short_body = input('У собаки короткое тело? ').casefold()
            if short_body == y:
                print('мопс')
            elif short_body == n:
                print('чихуахуа')
elif shorthair == y and height_50 == n:
    weight = input('Собака весит более 50 кг? ').casefold()
    if weight == y:
        print('датский дог')
    elif weight == n:
        print('фоксхаунд')
elif shorthair == n and height_50 == y:
    character = input('У собаки доброжелательный характер? ').casefold()
    if character == y:
        print('кокер-спаниэль')
    elif character == n:
        print('ирландский сеттер')
elif shorthair == n and height_50 == n:
    height_70 = input('У собаки рост менее 70 см? ').casefold()
    if height_70 == y:
        ears = input('У собаки длинные уши? ').casefold()
        if ears == y:
            print('большой вандейский грифон')
        elif ears == n:
            print('колли')
    elif height_70 == n:
        ginger = input('Окрас рыжий с белыми отметинами? ').casefold()
        if ginger == y:
            print('сенбернар')
        elif ginger == n:
            white = input('Белоснежный окрас? ').casefold()
            if white == y:
                print('ирландский волкодав')
            elif white == n:
                print('ньюфаундленд')