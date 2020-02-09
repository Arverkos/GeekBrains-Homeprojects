import json

with open('task07.txt', 'r', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт для чтения')

    firm_dict ={}
    profit_dict = {}
    i = 0
    total_profit = 0

    for line in f:
        info_list = line.split(' ')
        profit = int(info_list[2]) - int(info_list[3])
        if profit > 0:
            total_profit += profit
        i += 1
        firm_dict[info_list[0]] = profit

    average_profit = round(total_profit / i, 2)

    profit_dict = {'average_profit': average_profit}

    total_info_list = [firm_dict, profit_dict]
    print(total_info_list)

with open('task07-output.json', 'w', encoding='utf-8') as d:
    print(f'Файл {d.name} открыт для записи')

    json.dump(total_info_list, d)
    print('Данные записаны')

print(f'Программа завершена, файл {f.name} закрыт? - {f.closed}, файл {d.name} закрыт? - {d.closed}')
