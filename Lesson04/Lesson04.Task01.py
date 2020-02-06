from sys import argv


def salary(production, tax, bonus):
    result = (production * tax) + bonus
    return result


# При вводе первого аргумента необходимо ввести путь до файла Lesson04.Task01.py
print('Название скрипта:', argv[0])
print('Выработка в часах:', argv[1])
print('Оклад в час:', argv[2])
print('Премия:', argv[3])

print('Размер заработной платы:', salary(int(argv[1]), int(argv[2]), int(argv[3])))
