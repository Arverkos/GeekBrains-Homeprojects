n = int(input('Введите количество элементов в списке: '))
my_list = []

i = 0

for i in range(n):
    my_list.append(input('Введите элемент списка: '))

print('Введеный список', my_list)

for i in range(0, n, 2):
    if i == n - 1:
        break
    swap = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = swap

print('Список с перестановкой ', my_list)
