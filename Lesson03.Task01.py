def div(x, y):
    return x / y


num_1 = int(input('Введите число x (делимое): '))
num_2 = int(input('Введите число y (делитель): '))

if num_2 == 0:
    print('Деление на ноль невозможно')
else:
    print(div(num_1, num_2))
