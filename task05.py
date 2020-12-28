# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("file_task_05.txt", "w") as file_05:
    num_list = [str(randint(1, 100)) for _ in range(10)]  # Генерируем список из 10 случайных числе от 1 до 100
    print(f'{" ".join(num_list)}', file=file_05)  # Записываем 10 случайных чисел от 1 до 100 в файл

with open("file_task_05.txt") as file_05:
    num_list_2 = file_05.readline().split()
    sum_list_2 = 0
    for item in num_list_2:
        sum_list_2 += int(item)

    print(f'Сумма чисел в файле file_task_05.txt: {sum_list_2}')