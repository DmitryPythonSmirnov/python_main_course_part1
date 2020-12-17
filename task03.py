# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите номер месяца от 1 до 12: '))
while month not in list(range(13)):
    month = int(input('Вы ввели неправильной номер месяца. Введите номер месяца от 1 до 12: '))

# ----- Вариант через list -----
all_months = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

for ind in range(len(all_months)):
    if month in all_months[ind]:
        print(f'Результат через list: {seasons[ind]}')

# ----- Вариант через dict -----
seasons_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for key in seasons_dict:
    if month in seasons_dict[key]:
        print(f'Результат через dict: {key}')
