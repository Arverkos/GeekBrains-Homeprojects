with open('task03-salary.txt', 'r', encoding='utf-8') as f:
    print(f'Файл {f.name} открыт')
    print()

    total = 0
    count = 0

    for line in f:
        person_info = line.split(' ')
        person_salary = int(person_info[2])

        if person_salary < 20:
            print(f'Сотрудник {person_info[0]} имеет зарплату меньше 20 тыс. рублей')

        total += person_salary
        count += 1

    average_salary = round(total / count, 2)

    print(f'Средняя зарплата сотрудников составляет {average_salary} тыс. рублей')
    print()

print(f'Программа завершена, файл {f.name} закрыт? - {f.closed}')