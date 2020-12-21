# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    sorted_list = sorted([a, b, c])
    return sum(sorted_list[-2:])


a = 4
b = 2
c = 2

print(my_func(a, b, c))
