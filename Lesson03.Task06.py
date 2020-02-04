# Функция перевода первой буквы слова в Заглавную

def int_func(word):
    result = word.title() + ' '

    return result


# Функция преобразования исходной строки в требуемую

def my_func(str_loc):
    word_list = str_loc.split(' ')
    result = ''
    for el in word_list:
        result += int_func(el)
    return result


my_str = input('Введите строку из слов разделенных пробелом, все буквы в нижнем регистре: ')

print('Измененная строка:', my_func(my_str))
