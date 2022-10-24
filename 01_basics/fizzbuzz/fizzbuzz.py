crets={2:[0, 55],3:[55, 70],4:[70, 85],5:[85, 101]}
while True:
    a = input('Введите количество баллов: ')
    if a.isdigit():
        for key in crets:
            params=crets.get(key)
            if int(a) in range(params[0], params[1]):
                print('Оценка', key)
    else:
        break