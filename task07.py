# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

# Используется файл от преподавателя "text_7.txt".
# Считаем, что файл заполнен правильно, поэтому проверки на исключения при преобразовании типов и др. не производим

import json

with open("text_7.txt", encoding="utf-8") as file_07_in:
    firms_dict = {}
    good_firm_count = 0
    good_firm_income = 0
    for line in file_07_in:
        firm_list = line.split()
        firm_name = firm_list[0]
        firm_income = int(firm_list[2]) - int(firm_list[3])
        firms_dict[firm_name] = firm_income
        if firm_income > 0:
            good_firm_count += 1
            good_firm_income += firm_income

    average_income = round((good_firm_income / good_firm_count), 2)
    av_income_dict = {"average_profit": average_income}
    result_list = [firms_dict, av_income_dict]

    with open("file_task_07_out.json", "w", encoding="utf-8") as file_07_out:
        json.dump(result_list, file_07_out, indent=4, ensure_ascii=False)
