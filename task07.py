# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result


for el in fact(5):  # Вместо 5 подставляем нужное число
    print(el)
