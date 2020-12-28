#  Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng_file = open("text_4.txt")
rus_file = open("text_4_rus.txt", "w", encoding="utf-8")
eng_rus_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре"}


for line in eng_file:
    temp_list = line.split()
    temp_list[0] = eng_rus_dict[temp_list[0].lower()].capitalize()
    print(f'{" ".join(temp_list)}', file=rus_file)

eng_file.close()
rus_file.close()


