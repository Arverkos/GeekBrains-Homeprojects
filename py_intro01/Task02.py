time = int(input('Введите время в секундах: '))

hours = time // 3600

minutes = time % 3600 // 60

seconds = (time % 3600) % 60

print('Переведенное время (1-й способ):', "%02d:%02d:%02d" % (hours, minutes, seconds))

print('Переведенное время (2-й способ):', '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

print(f"Переведенное время (3-й способ): {hours:#02d}:{minutes:#02d}:{seconds:#02d}")