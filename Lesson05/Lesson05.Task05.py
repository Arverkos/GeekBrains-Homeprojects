# Первая часть задачи - создание текстового файла
with open('task05.txt', 'w', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт для записи, выполняйте дальнейшие инструкции')

    numbers = input('Введите последовательность чисел, разделенных пробелами: ')
    f.write(numbers)

print(f'Данные записаны, первая часть задачи завершена, файл {f.name} закрыт? - {f.closed}')
print()

# Вторая часть задачи - подсчет суммы чисел в созданом файле
with open('task05.txt', 'r', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт для чтения')

    numbers = f.read()
    numbers_list = numbers.split(' ')
    sum = 0
    for el in numbers_list:
        sum += int(el)
    print(sum)

print(f'Программа завершена, файл {f.name} закрыт? - {f.closed}')