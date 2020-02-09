with open('task02.txt', 'r', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт')
    print()

    i = 0

    for line in f:
        i += 1
        word_number = len(line.split(' '))
        print(f'{i}-я строка содержит {word_number} слов(-а)')

    print(f'Файл содержит {i} строк')

print(f'Программа завершена, файл {f.name} закрыт? - {f.closed}')