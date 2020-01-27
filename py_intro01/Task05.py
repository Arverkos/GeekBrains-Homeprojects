revenue = int(input('Введите размер выручки компании, млн. руб.: '))
costs = int(input('Введите размер издержек компании, млн. руб.: '))

if revenue > costs:
    print('Фирма работает с прибылью')
    print('Рентабельность составляет:', (revenue - costs) / revenue)
elif revenue == costs:
    print('Фирма работает в "ноль"')
else:
    print('Фирма работает с убытком')

staff_number = int(input('Введите количество сотрудников: '))
profit_per_staff = (revenue-costs) / staff_number
print('Размер прибыли на каждого сотрудника, млн. руб.:', profit_per_staff)