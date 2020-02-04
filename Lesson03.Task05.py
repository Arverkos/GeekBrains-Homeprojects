# Вводим функцию, суммирующую элементы строки поэлементно:

def my_func(line_loc, stop):
    my_list = line_loc.split(' ')
    result = 0
    for el in my_list:
        if el != stop:
            result += int(el)
        else:
            break
    return result


# Основная часть

# Запрашиваем "стоп-символ"

stop_symbol = input('Введите "стоп-символ": ')

line = []

sum = 0

# "Пока "стоп-символа" нет в строке выполняем цикл:

while stop_symbol not in line:
    # Вводим строку чисел с пробелами:

    line = input('Введите строку чисел с пробелами: ')

    # С помощью фукции my_func суммируем элементы по условию задачи:

    sum += my_func(line, stop_symbol)

    # Выводим текущее значение суммы:

    print('Текущее значение суммы: ', sum)

# Выводим окончательное значение функции:

print()
print('Сумма чисел по условию: ', sum)
