# Структура данных "Товары"

# Запрашиваем количество товаров:

number_of_product = int(input('Введите количество товаров: '))

product_table = []

# Формируем продуктовую таблицу по условию задачи:

for i in range(number_of_product):
    product_line = ()
    product_feature = {"Название": '', "Стоимость": 0, "Количество": 0, "Ед. изм.": ''}
    for key in product_feature.keys():
        product_feature[key] = input('Введите {} продукта №{}: '.format(key, i + 1))
    product_feature["Стоимость"] = int(product_feature["Стоимость"])  # Переводим тип данных "Стоимость" в int
    product_feature["Количество"] = int(product_feature["Количество"])  # Переводим тип данных "Количество" в int
    product_line = (i + 1, product_feature)
    product_table.append(product_line)

# Выводим таблицу в требуемом формате:

print()
print('Продуктовая таблица')
print()

for i in range(number_of_product):
    print(product_table[i])

# Проводим аналитику товаров по условию задачи

# Создаем списки значений для каждой характеристики

name_list = []
price_list = []
quantity_list = []
unit_list = []

# Заполняем их

for product_line in product_table:
    name_list.append(product_line[1].get('Название'))
    price_list.append(product_line[1].get('Стоимость'))
    quantity_list.append(product_line[1].get('Количество'))
    unit_list.append(product_line[1].get('Ед. изм.'))

# Формируем словарь "характеристика - список значений"

product_dict = {'Название': name_list,
                'Стоимость': price_list,
                'Количество': quantity_list,
                'Ед. изм.': list(set(unit_list))
                }

# Выводим получившийся словарь

print()
print('Вывод данных в заданном формате')
print()

for key, value in product_dict.items():
    print('{}: {}'.format(key, value))