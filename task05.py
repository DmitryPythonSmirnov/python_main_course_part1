# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def my_mult(prev_el, el):
    return prev_el * el

list_1 = [el for el in range(100, 1001) if el % 2 == 0]
print(list_1)
print(reduce(my_mult, list_1))
