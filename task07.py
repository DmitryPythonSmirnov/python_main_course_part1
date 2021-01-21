"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, a, b):
        self.a = a  # Действительная часть
        self.b = b  # Мнимая часть

    def __add__(self, other):
        res_a = self.a + other.a
        res_b = self.b + other.b
        return complex(res_a, res_b)

    def __mul__(self, other):
        res_a = self.a * other.a - self.b * other.b
        res_b = self.a * other.b + self.b * other.a
        return complex(res_a, res_b)


num_1 = ComplexNum(1, 2)
num_2 = ComplexNum(3, 4)
print(num_1 + num_2)
print(num_1 * num_2)
