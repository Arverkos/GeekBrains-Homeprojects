class NullDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    inp_num_1 = int(input('Введите число (делимое): '))
    inp_num_2 = int(input('Введите число (делитель): '))
    if int(inp_num_2) == 0:
        raise NullDiv('Делитель равен нулю, делить на ноль нельзя!')
except ValueError:
    print('Введенное значение не число!')
except NullDiv as err:
    print(err)
else:
    print(f'Все хорошо. Результат деления {round(inp_num_1 / inp_num_2, 2)}')
