eng_rus_num = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('task04-input.txt', 'r', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт для чтения')
    with open('task04-output.txt', 'w', encoding='utf-8') as d:
        print(f'Файл {d.name} открыт для записи')
        print()

        for line in f:
            line_list = line.split(' ')
            line_list[0] = eng_rus_num[line_list[0]]
            d.writelines(line_list)

print(f'Программа завершена, файл {f.name} закрыт? - {f.closed}, файл {d.name} закрыт? - {d.closed}')
