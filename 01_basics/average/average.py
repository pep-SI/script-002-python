def digit_list():
    print('Введите числа для определения среднего значения, концом ввода принимается пустая строка')
    out_list = []
    count = 0
    while True:
        count+=1
        data = input('{} Число: '.format(count))
        if data.isdigit():
            out_list.append(int(data))
        elif data != '':
            print('Принимаются только числа!' )
        else:
            return out_list

def average(digit_list = list):
    summ=0
    for num in digit_list:
        summ+=num
    if digit_list:
        return summ/len(digit_list)
    else:
        return 0

print('Среднее значение всех чисел: {}'.format(average(digit_list())))