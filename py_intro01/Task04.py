#Вводим число n

n = int(input('Введите число n (n - целое, положительное): '))

#Далее необходимо найти количество цифр в числе

figure_index = 10

number_of_figure = 1

while True:
 if n // figure_index == 0:
     break
 else:
     figure_index = figure_index*10
     number_of_figure += 1

#Печатаем количество цифр в числе

print('Количество цифр в числе n', number_of_figure)

max = 0 #Переменная, которой присваивается максимальное значение среди цифр числа n
i = 1  #Шаг проверки числа

#Находим максимальное число перебирая цифры в числе

while i <= number_of_figure:
 if i == 1:
     current_figure = n % 10
 else:
     current_figure = n % 10**i // 10**(i-1)
 i += 1
 if current_figure > max:
     max = current_figure

print('Максимальная цифра в числе n:', max)