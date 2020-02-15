from itertools import cycle
import time


class TrafficLight:
    __colour = {'Красный': 7,
                'Желтый': 2,
                'Зеленый': 10}

    def running(self):
        number = int(input('Светофор начинает работу, введите количество циклов "КЖЗ": '))
        c = 0
        for el in cycle(self.__colour):
            if el == 'Красный':
                print(f'горит {el} - остановка движения!')
                time.sleep(self.__colour['Красный'])
            elif el == 'Желтый':
                print(f'горит {el} - приготовтесь!')
                time.sleep(self.__colour['Желтый'])
            elif el == 'Зеленый':
                print(f'горит {el} - можно ехать!')
                time.sleep(self.__colour['Зеленый'])
                c += 1
            if c == number:
                print('Работа сфетофора завершена')
                break


svetofor = TrafficLight()

svetofor.running()
