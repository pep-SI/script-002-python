#Так так так, настало время изучить такую штуку как классы
#Что я понял, порочитав пару статей? Класс это функции в функцие, но с приколами
#Попробую написать класс для простого ведения логов с параметрами
from datetime import datetime

class DeLog:

    #Эта функция выполняется сразу же, при обращении к классу или создании его экземпляра
    #param - принимает значение "rew", означающее перезапись файла лога
    def __init__(self, name='NONAME', datetype='dt', param=None):
        self.param = param
        self.name = name
        if self.param == 'rew':
            with open(self.name+'.log', 'w') as file:
                None
        if datetype == 'dt':
            self.datetype = '%d.%m.%Y|%H:%M:%S   '
        elif datetype == 'd':
           self.datetype = '%d.%m.%Y   '
        elif datetype == 't':
            self.datetype = '%H:%M:%S   '

    def loging(self, data):
        datalog = data
        with open(self.name+'.log', 'a') as file:
            file.write(datetime.today().strftime(self.datetype)+str(datalog)+'\n')
            return(data)

    def debug(self, data):
        print(data)
        return data

if __name__ == '__main__':

#Эта конструкция позволяет определить, запущен ли данный код отдельно, или он импортирован
#в другой код. __name__ определяет "имя" скрипта. __main__ основнвной скрипт, который запущен
#Внизу приведен пример применения модуля

    vlog = DeLog('a','logTimed','t')

    vlog.loging('good day, yes? ')
    print(vlog.debug(datetime.today()).strftime('%d.%m.%Y|%H:%M   '))

    
