class Data:

    @classmethod
    def data_to_num(cls, data):
        data_list = data.split('.')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])
        print(f'число {day, type(day)}, месяц {month, type(month)}, год {year, type(year)}')

    @staticmethod
    def check_data(data):
        data_list = data.split('.')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])

        if (day > 0) and (day < 30):
            print(f'число даты - {day} - лежит в допустимых пределах')
        else:
            print(f'число даты - {day} - не лежит в допустимых пределах!')

        if (month >= 1) and (month <= 12):
            print(f'месяц даты - {month} - лежит в допустимых пределах')
        else:
            print(f'месяц даты - {month} - не лежит в допустимых пределах!')

        if year > 0:
            print(f'год даты - {year} - лежит в допустимых пределах')
        else:
            print(f'год даты - {year} - не лежит в допустимых пределах!')


data_1 = input('Введите дату в формате dd.mm.yyyy: ')

Data.data_to_num(data_1)

Data.check_data(data_1)
