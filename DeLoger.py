#Так так так, настало время изучить такую штуку как классы
#Что я понял, порочитав пару статей? Класс это функции в функцие, но с приколами
#Попробую написать класс для простого ведения логов с параметрами
from datetime import datetime

class DeLog:
    '''Объект класса DeLog представляет собой фунции логирования и дебага.
    При создании экземпляра класса, он принимает в качестве аргументов параметры
    логирования: имя лога, формат даты и форма записи лога в файл.
    rew позволяет перезаписывать лог при каждом запуске программы, в которой он применен,
    что позволяет отображать актуальную информацию по последней запущенной сессии.'''

    #Эта функция выполняется сразу же, при обращении к классу или создании его экземпляра
    def __init__(self, name:str = 'NONAME' , datetype:str = 'dt', param:str = None):
        self.__param = param
        self.__name = name
        if self.__param == 'rew':
            with open(self.__name+'.log', 'w') as file:
                pass
        if datetype == 'dt':
            self.__datetype = '%d.%m.%Y|%H:%M:%S   '
        elif datetype == 'd':
           self.__datetype = '%d.%m.%Y   '
        elif datetype == 't':
            self.__datetype = '%H:%M:%S   '

    def loging(self, data: str) -> str:
        with open(self.__name+'.log', 'a') as file:
            file.write(datetime.today().strftime(self.__datetype)+str(data)+'\n')
            return(data)

    def debug(self, data: str) -> str:
        print(data)
        return data

if __name__ == '__main__':

#Эта конструкция позволяет определить, запущен ли данный код отдельно, или он импортирован
#в другой код. __name__ определяет "имя" скрипта. __main__ основнвной скрипт, который запущен
#Внизу приведен пример применения модуля

    print(DeLog.__doc__)
    vlog = DeLog('logTimed','t')

    vlog.loging('good day, yes? ')
    print(vlog.debug(datetime.today()).strftime('%d.%m.%Y|%H:%M   '))

    
