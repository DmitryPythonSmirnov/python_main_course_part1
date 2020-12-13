# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

input_seconds = int(input('Введите количество секунд: '))
hours = input_seconds // 3600
minutes = (input_seconds - hours * 3600) // 60
seconds = input_seconds - hours * 3600 - minutes * 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
