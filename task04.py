"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Warehouse:
    pass


class OfficeEquip:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


class Printer(OfficeEquip):
    def print_page(self):
        print("Печать страницы.")


class Scanner(OfficeEquip):
    def scan_page(self):
        print("Сканирование страницы.")


class Copier(OfficeEquip):
    def copy_page(self):
        print("Копирование страницы.")
