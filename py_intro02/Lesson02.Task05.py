current_rating = [7, 5, 5, 4, 3, 3, 3, 1]

print('Начальные значения рейтинга')
print(current_rating)

new = int(input('Введите новое значение рейтинга (Натуральное число): '))

for i in range(len(current_rating)):
    if new > current_rating[i]:
        current_rating.insert(i, new)
        break

    elif i == len(current_rating) -1 and new <= current_rating[i]:
        current_rating.append(new)

print('Измененные значения рейтинга')
print(current_rating)
