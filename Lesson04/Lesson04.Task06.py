from itertools import count, cycle

"Первая часть задачи"
num = int(input('Введите число с которого необходимо начать: '))
for el in count(num):
    if el == num + 10:
        break
    else:
        print(el)

"Вторая часть задачи"
my_list = ['a', 'b', 'c', 'd']
c = 0
for el in cycle(my_list):
    if c < 10:
        print(el)
    else:
        break
    c += 1
