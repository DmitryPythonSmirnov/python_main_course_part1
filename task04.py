# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    if (type(x) == float or type(x) == int)  and type(y) == int:
        if x > 0 and y < 0:
            return x ** y
        else:
            return '"x" и/или "y" не соответствуют условию "x > 0 and y < 0".'
    else:
        return '"x" и/или "y" не соответствуют условию задачи по своему типу данных.'


def my_func2(x, y):
    if (type(x) == float or type(x) == int)  and type(y) == int:
        if x > 0 and y < 0:
            result = x
            for i in range(abs(y)-1):
                result *= x
            return 1 / result
        else:
            return '"x" и/или "y" не соответствуют условию "x > 0 and y < 0".'
    else:
        return '"x" и/или "y" не соответствуют условию задачи по своему типу данных.'


x = 3
y = -3
print(my_func(x, y))
print(my_func2(x, y))
