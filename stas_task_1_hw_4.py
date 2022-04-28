text_1 = input('Пожалуйста введите Ваш текст ')

if len(text_1) >= 2:
    print(text_1[0:2], text_1[::-1][0:2], sep='')
elif len(text_1) < 2:
    print('Ваша строка слишком короткая - %s' % (text_1))
