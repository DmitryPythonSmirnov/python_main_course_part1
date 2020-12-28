# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_01 = open('file_task_01.txt', 'w', encoding='utf-8')

while True:
    input_string = input('Введите информацию и нажмите Enter. Для прекращения ввода просто нажмите Enter: ')
    if input_string == '':
        break
    input_string += '\n'  # Добавляем перевод строки
    file_01.write(input_string)

file_01.close()
