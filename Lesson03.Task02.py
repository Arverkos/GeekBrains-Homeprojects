def person_info(name_loc, surname_loc, birth_year_loc, city_loc, email_loc, tel_loc):
    print(f'{name_loc} {surname_loc} {birth_year_loc} {city_loc} {email_loc} {tel_loc}')


print('Введите данные пользователя')
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('Введите email: ')
tel = input('Введите телефон: ')

# По условию функция должна принимать параметры, как именованные аргументы

person_info(name_loc=name, surname_loc=surname, birth_year_loc=birth_year, city_loc=city, email_loc=email, tel_loc=tel)
