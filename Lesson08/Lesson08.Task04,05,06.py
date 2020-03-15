class ModelInpError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DataInpError(Exception):
    def __init__(self, txt):
        self.txt = txt


class PriceInpError(Exception):
    def __init__(self, txt):
        self.txt = txt


class QuantInpError(Exception):
    def __init__(self, txt):
        self.txt = txt


class ColourInpError(Exception):
    def __init__(self, txt):
        self.txt = txt


"""Создаем класс "Склад" куда будут производится записи о поступлении товаров"""


class Warehouse:
    """Товары различных типов будут поступать в различные департаменты,
        которые реализованы в виде словаря с ключами (названия отделов),
        в которые будут вноситься записи о поступлениях товаров.
        Каждое поступление товара записывается в формате "словарь" с ключами:
        "модель", "дата поступления", "цена", "количество", "дополнительная опция"."""

    def __init__(self):
        self.catalog = {'отдел принтеров': [],
                        'отдел сканеров': [],
                        'отдел компьютеров': []
                        }

    """Определяем метод - добавление записи о товаре в каталог склада"""

    def add_item(self, model, data, price, quantity, colour):
        if model == 'принтер':
            self.catalog['отдел принтеров'].append({'Модель': model,
                                                    'Дата поставки': data,
                                                    'Стоимость': int(price),
                                                    'Количество': int(quantity),
                                                    'Цвет': colour
                                                    })

        if model == 'сканнер':
            self.catalog['отдел сканеров'].append({'Модель': model,
                                                   'Дата поставки': data,
                                                   'Стоимость': int(price),
                                                   'Количество': int(quantity),
                                                   'Цвет': colour
                                                   })

        if model == 'компьютер':
            self.catalog['отдел компьютеров'].append({'Модель': model,
                                                      'Дата поставки': data,
                                                      'Стоимость': int(price),
                                                      'Количество': int(quantity),
                                                      'Цвет': colour
                                                      })

    def get_printer(self):
        print('Записи поступления товаров в отдел "Принтеры"')
        for el in self.catalog['отдел принтеров']:
            print(el)

    def get_scanner(self):
        print('Записи поступления товаров в отдел "Сканнеры"')
        for el in self.catalog['отдел сканеров']:
            print(el)

    def get_computer(self):
        print('Записи поступления товаров в отдел "Компьютеры"')
        for el in self.catalog['отдел компьютеров']:
            print(el)

    @staticmethod  # Статический метод проверки даты поставки
    def check_data(data):
        data_list = data.split('.')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])

        if (day > 0) and (day < 30) and (month >= 1) and (month <= 12) and year > 0:
            return True
        else:
            return False


class OfficeTec:
    def __init__(self, model, data, price, quantity):
        self.model = model
        self.price = price
        self.count = quantity
        self.data = data


class Printer(OfficeTec):
    def __init__(self, model, data, price, quantity, colour):
        super().__init__(model, price, quantity, data)
        self.colour = colour


class Scanner(OfficeTec):
    def __init__(self, model, data, price, quantity, colour):
        super().__init__(model, price, quantity, data)
        self.colour = colour


class Computer(OfficeTec):
    def __init__(self, model, data, price, quantity, memory):
        super().__init__(model, price, quantity, data)
        self.memory = memory


Warehouse_1 = Warehouse()

while True:
    inp_check = input('Введите "стоп" для остановки процесса внесения записей в каталог,\n '
                      'если нужны дополнительные записи нажмите "Enter": ')
    if inp_check == 'стоп':
        break

    """Осуществляем поочередный ввод данных с обходом некорректных случаев ввода"""

    try:
        inp_model = input('Введите тип техники в партии "принтер"/"сканнер"/"компьютер": ')
        if inp_model not in ['принтер', 'сканнер', 'компьютер']:
            raise ModelInpError('Введено недопустимое название модели, начните ввод записи заново')
    except ModelInpError as err:
        print(err)
        continue

    try:
        inp_data = input('Введите дату поставки партии: ')
        if not Warehouse.check_data(inp_data):
            raise DataInpError('Введена недопустимая дата поставки партии, начните ввод записи заново')
    except DataInpError as err:
        print(err)
        continue
    except ValueError:
        print('Введена недопустимая дата поставки партии, начните ввод записи заново')
        continue

    try:
        inp_price = int(input('Введите стоимость единицы модели в партии: '))
        if inp_price < 0:
            raise PriceInpError('Введена некорректная стоимость, начните ввод записи заново')
    except ValueError:
        print('Введена некорректная стоимость, начните ввод записи заново')
        continue
    except PriceInpError as err:
        print(err)
        continue

    try:
        inp_quantity = int(input('Введите количество товара в партии: '))
        if inp_quantity < 0:
            raise QuantInpError('Введено некорректное количество, начните ввод записи заново')
    except ValueError:
        print('Введено некорректное количество, начните ввод записи заново')
        continue
    except QuantInpError as err:
        print(err)
        continue

    try:
        inp_colour = input('Введите цвет моделей в партии "белый"/ "черный"/ "золотой": ')
        if inp_colour not in ['белый', 'черный', 'золотой']:
            raise ColourInpError('Введено недопустимое название цвета, начните ввод записи заново')
    except ColourInpError as err:
        print(err)
        continue

    """Присваиваем класс товару в зависимости от названия модели"""
    if inp_model == 'принтер':
        new = Printer(inp_model, inp_data, inp_price, inp_quantity, inp_colour)
    if inp_model == 'сканер':
        new = Scanner(inp_model, inp_data, inp_price, inp_quantity, inp_colour)
    if inp_model == 'компьютер':
        new = Computer(inp_model, inp_data, inp_price, inp_quantity, inp_colour)

    """Вносим информацию по партии в каталог склада"""
    Warehouse_1.add_item(inp_model, inp_data, inp_price, inp_quantity, inp_colour)
    print('Информация о партии внесена в каталог')

"""После завершения цикла выводим сообщение о завершении процесса записи"""
print('Внесение записей в журнал завершено')

"""Далее реализуем механизм запроса поставок в разрезе по отделам"""
check_item = input('О поставках в какой отдел вы бы хотели получить информацию: принтеры/сканнеры/компьютеры? ')
if check_item == 'принтеры':
    Warehouse_1.get_printer()
if check_item == 'сканнеры':
    Warehouse_1.get_scanner()
if check_item == 'компьютеры':
    Warehouse_1.get_computer()
