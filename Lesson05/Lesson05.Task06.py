with open('task06.txt', 'r', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт для чтения')

    new_dict = {}

    for line in f:
        sum = 0
        subj_list = line.split(':')  # Сначала делим входящую строку по знаку ":" - так отделяем название предмета
        subj_name = subj_list[0]  # Записываем название предмета в отдельную переменную
        type_lesson = subj_list[1].split(' ')  # Вторую часть входящей строки делим сначала пробелом, затем '(',
        for lesson in type_lesson:             # этому знаку всегда прешествуют цифры.
            num_lesson = lesson.split('(')
            for el in num_lesson:              # Далее, отделив цифры, считаем сумму этих цифр по каждой строке
                if el.isdigit():
                    sum += int(el)
        new_dict[subj_name] = sum

print(new_dict)

print(f'Программа завершена, файл {f.name} закрыт? - {f.closed}')
