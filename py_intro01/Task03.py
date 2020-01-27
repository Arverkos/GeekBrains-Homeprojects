# Вводим число, оно должно быть больше 0 и целое

number = int(input('Введите целое число больше 0: '))

#Введеное Число может быть больше 10, например 543, в таком случае будет необходимо найти сумму 543 + 543543 + 543543543

#Тогда нам предварительно необходимо найти количество цифр в числе

figure_index = 10

number_of_figure = 1

while True:
 if number // figure_index == 0:
     break
 else:
     figure_index = figure_index*10
     number_of_figure += 1

#Печатаем число цифр в введеном числе для проверки

print('Количество цифр числе:', number_of_figure)

#Получаем сумму по условию задачи

sum = number + (number*(10**number_of_figure) + number) + (number*(10**(number_of_figure*2)) + number*(10**number_of_figure) + number)

print(sum)