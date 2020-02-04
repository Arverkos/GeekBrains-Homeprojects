def my_func(x, y, z):
    my_list = sorted([x, y, z])
    result = int(my_list[1]) + int(my_list[2])
    return result


num_1 = input('Введите число №1: ')
num_2 = input('Введите число №2: ')
num_3 = input('Введите число №3: ')

print('Сумма 2-х наибольших чисел', my_func(num_1, num_2, num_3))
