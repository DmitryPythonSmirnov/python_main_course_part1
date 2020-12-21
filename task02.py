# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, last_name, year, city, email, phone):
    print(f'Имя: {name}, Фамилия: {last_name}, год рождения: {year},',
          f'город проживания: {city}, email: {email}, телефон: {phone}')

# name = 'Dmitry'
# last_name = 'Smirnov'
# year = '1982'
# city = 'Saint Petersburg'
# email = 'dimasm2001@mail.ru'
# phone = '1122334455'

user_data(name='Dmitry', last_name='Smirnov', year='1982', city='Saint Petersburg', \
          email='dimasm2001@mail.ru', phone = '1122334455')
