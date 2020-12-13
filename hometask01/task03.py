# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input('Введите целое положитальное число: '))
num_1 = num
num_2 = int(str(num) + str(num))
num_3 = int(str(num) + str(num) + str(num))
total = num_1 + num_2 + num_3
print(f'Сумма чисел {num_1} + {num_2} + {num_3} = {total}')
