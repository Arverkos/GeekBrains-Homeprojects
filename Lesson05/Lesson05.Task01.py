with open('task01.txt', 'w', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт, следуйте дальнейшим указаниям')
    print()

    while True:

        new_str = input('Введите новую строку для записи в файл: ')
        f.write(new_str + '\n')

        if new_str == '':
            break

print(f'Программа завершена, файл {f.name} закрыт? - {f.closed}')
