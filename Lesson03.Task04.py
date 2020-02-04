# Первый способ:

def my_func_1(x, y):
    result = x ** y
    return round(result, 5)


# Второй способ:

def my_func_2(x, y):
    result = 1

    for i in range(abs(y)):
        result *= 1 / x

    return round(result, 5)


num_1 = float(input('Введите действительное положительное число x: '))
num_2 = int(input('Введите целое отрицательное число y: '))

print('Вывод первым способом: ', my_func_1(num_1, num_2))

print('Вывод вторым способом: ', my_func_2(num_1, num_2))
