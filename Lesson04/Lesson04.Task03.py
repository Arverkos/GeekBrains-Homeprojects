# Вопрос к условию задачи: границы интервала включены или нет?
# В данном случае я решил, что да, поэтому правую границу выставил не "240", а "241",
# чтобы включить "240" в указанный предел

print([el for el in range(20,241) if (el % 20 == 0) or (el % 21 == 0)])