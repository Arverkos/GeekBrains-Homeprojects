import math

#Функция формирования факториалов в формате генератора
def fibo_gen(num):
    for el in range(num):  #Начинаем всегда с "0", факториал "0" - единица
        num_factor = math.factorial(el)
        yield num_factor

number = int(input('Введите количество чисел, которые необходимо вывести: '))

#Вывод чисел
for el in fibo_gen(number):
    print(el)
