# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count, cycle

my_iter_1 = count(3)
print('')
for i in range(5):
    print(next(my_iter_1), end=' ')

print()  # Для переноса строки после предыдущего вывода

my_iter_2 = cycle([1, 2, 3, 4, 5])
for i in range(20):
    print(next(my_iter_2), end=' ')
