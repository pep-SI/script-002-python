import os

def get_course(path):
    course = []
    with open(path) as file:
        for line in file:
            course.append(line.replace('\n','').split(':'))
    return course

def add_course(path, course:list):
    new_elem = []
    while True:
        new_name = input('Новое название: ')
        if new_name == '':
            return course
        elif new_name.isalpha():
            new_elem.append(new_name)
            break
        else:
            print('Принимаются строковые значения!')
    while True:
        new_course = input('Новое значение: ').replace(',','.')
        if new_course == '':
            return course
        elif new_course.replace('.','').isdigit():
            new_elem.append(new_course)
            break
        else:
            print('Принимаются числовые значения!')
    course.append(new_elem)
    write_course(path, course)
    return course

def del_course(path, course:list):
    print('Для удаления курса из списка, введите номер по порядку.')
    num = list_course(course)
    if num:
        course.pop(num-1)
        write_course(path, course)
        return course
    return course

def convert_course(course: list):
    print('Выберете курс для конвертации')
    num = list_course(course)
    if num:
        while True:
            rubs = input('Введите сумму в рублях(Enter для выхода): ').replace(',','.')
            if rubs == '':
                break
            elif rubs.replace('.','').isdigit():
                resul = float(rubs) / float(course[num-1][1])
                print(round(resul, 2))
            else:
                print('Принимаются числовые значения!')
    return True

def write_course(path, course):
    with open(path, 'w') as file:
        for element in course:
            file.write('{}:{}\n'.format(element[0],element[1]))

def list_course(course):
    counter = 0
    for element in course:
        counter+=1
        print('{}) {} : {}'.format(counter, element[0], element[1]))
    print('0) Выход')
    while True:
        numb = input('Введите номер курса: ')
        if not (numb.isdigit() and int(numb) in range(len(course)+1)):
            print('Принмаются значения от 0 до {}!'.format(len(course)))
            continue
        elif numb == 0:
            return 0
        return int(numb)

if __name__ == '__main__':
    abspath = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.join(abspath, 'course.cfg')
    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write('RUB:1')
    course = get_course(path)
    while True:
        print('Программа работает с курсом валют, выберите действия:\n1) Посчитать курс к рублю\n2) Добавить курс\n3) Удалить курс\n0) Выход')
        do = input('Введите номер действия: ')
        if do == '' or do == '1':
            convert_course(course)
        elif do == '2':
            add_course(path, course)
        elif do == '3':
            del_course(path, course)
        elif do == '0':
            break
        else:
            print('Введите значения от 0 до 3')

#print('Программа конвертации валюты по курсу, заданному пользователем')
#course = input('Введите курс EUR/RUB: ')
#rubs = input('Введите сумму в рублях: ')
#resul = float(rubs)/float(course)
#print('По курсу {} на {} рублей вы купите {} евро.'.format(course, rubs, resul))