current_distance = int(input('Текущий размер пробегаемой дистанции, км: '))
target_distance = int(input('Целевой размер пробегаемой дистанции, км: '))

progress_index = 1.1

day = 1

while current_distance < target_distance:
    day += 1
    current_distance *= progress_index

print('День достижения размера целевой пробегаемой дистанции:', day)