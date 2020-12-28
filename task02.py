# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("file_task_02.txt", "r", encoding='utf-8') as file_02:
    count_lines = 0
    for line in file_02:
        count_words = len(line.split())
        count_lines += 1
        print(f'Количество слов в строке {count_lines}: {count_words}')

    print(f'Всего строк в файле: {count_lines}')

