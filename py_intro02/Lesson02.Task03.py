# Решение через тип list
print('Решение через тип данных list')

year_period_list = [
    ['Winter', '12', '1', '2'],
    ['Spring', '3', '4', '5'],
    ['Summer', '6', '7', '8'],
    ['Autumn', '9', '10', '11']
]

month = input('Введите номер месяца (например 12 - декабрь): ')

for period in year_period_list:
    if month in period:
        print('Время года: ', period[0])

# -------------------------------------------------------------------------
# Решение через тип dict

print()
print('Решение через тип данных dict')

year_period_dict = {
    'Winter': ['12', '1', '2'],
    'Spring': ['3', '4', '5'],
    'Summer': ['6', '7', '8'],
    'Autumn': ['9', '10', '11']
}

month = input('Введите номер месяца (например 12 - декабрь): ')

for period, period_monthes in year_period_dict.items():
    if month in period_monthes:
        print('Время года: ', period)
