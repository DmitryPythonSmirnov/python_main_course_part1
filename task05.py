"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""


class Warehouse:
    whs_equip_qty = {"printers": 0, "scanners": 0, "copiers": 0}  # Оборудование на складе
    depart_1 = {"printers": 0, "scanners": 0, "copiers": 0}  # Оборудование в Отделе1
    depart_2 = {"printers": 0, "scanners": 0, "copiers": 0}  # Оборудование в Отделе2

    # Прием принтеров на склад
    @classmethod
    def get_printers(cls, num):
        cls.whs_equip_qty["printers"] += num
        print(f"Получили на склад {num} принтеров.")

    # Прием сканеров на склад
    @classmethod
    def get_scanner(cls, num):
        cls.whs_equip_qty["scanners"] += num
        print(f"Получили на склад {num} сканеров.")

    # Прием копиров на склад
    @classmethod
    def get_copier(cls, num):
        cls.whs_equip_qty["copiers"] += num
        print(f"Получили на склад {num} копиров.")

    # Передача принтеров в отдел
    @classmethod
    def transfer_printers(cls, depart_name, num):
        if cls.whs_equip_qty["printers"] == 0:
            print("На складе нет принтеров.")
        elif num > cls.whs_equip_qty["printers"]:
            print("Вы запросили принтеров больше, чем есть на складе.")
        else:
            if depart_name == "depart_1":
                cls.whs_equip_qty["printers"] -= num
                cls.depart_1["printers"] += num
                print(f"Передали в Отдел1 {num} принтеров.")
            elif depart_name == "depart_2":
                cls.whs_equip_qty["printers"] -= num
                cls.depart_2["printers"] += num
                print(f"Передали в Отдел2 {num} принтеров.")
            else:
                print("Такого отдела не существует.")

    # Передача сканеров в отдел
    @classmethod
    def transfer_scanner(cls, depart_name, num):
        if cls.whs_equip_qty["scanners"] == 0:
            print("На складе нет сканеров.")
        elif num > cls.whs_equip_qty["scanners"]:
            print("Вы запросили сканеров больше, чем есть на складе.")
        else:
            cls.whs_equip_qty["scanners"] -= num
            if depart_name == "depart_1":
                cls.depart_1["scanners"] += num
            elif depart_name == "depart_2":
                cls.depart_2["scanners"] += num
            else:
                print("Такого отдела не существует.")

    # Передача копиров в отдел
    @classmethod
    def transfer_copier(cls, depart_name, num):
        if cls.whs_equip_qty["copiers"] == 0:
            print("На складе нет копиров.")
        elif num > cls.whs_equip_qty["copiers"]:
            print("Вы запросили копиров больше, чем есть на складе.")
        else:
            cls.whs_equip_qty["copiers"] -= num
            if depart_name == "depart_1":
                cls.depart_1["copiers"] += num
            elif depart_name == "depart_2":
                cls.depart_2["copiers"] += num
            else:
                print("Такого отдела не существует.")


whs_1 = Warehouse()  # Объект склада
print(f"Оборудование на складе: {whs_1.whs_equip_qty}")
print(f"Оборудование в Отделе1: {whs_1.depart_1}")
print(f"Оборудование в Отделе2: {whs_1.depart_2}")
print()
whs_1.get_printers(5)  # Принимаем на склад 5 принтеров
whs_1.get_scanner(7)  # Принимаем на склад 5 сканеров
whs_1.get_copier(9)  # Принимаем на склад 9 копиров
print(f"Оборудование на складе: {whs_1.whs_equip_qty}")
print(f"Оборудование в Отделе1: {whs_1.depart_1}")
print(f"Оборудование в Отделе2: {whs_1.depart_2}")
print()
whs_1.transfer_printers("depart_1", 2)  # Передаем 2 принтера в Отдел1
print(f"Оборудование на складе: {whs_1.whs_equip_qty}")
print(f"Оборудование в Отделе1: {whs_1.depart_1}")
print(f"Оборудование в Отделе2: {whs_1.depart_2}")
print()
whs_1.transfer_printers("depart_2", 1)  # Передаем 1 принтер в Отдел2
print(f"Оборудование на складе: {whs_1.whs_equip_qty}")
print(f"Оборудование в Отделе1: {whs_1.depart_1}")
print(f"Оборудование в Отделе2: {whs_1.depart_2}")
print()
whs_1.transfer_printers("depart_3", 2)  # Пытаемся передать 2 принтера в несуществующий отдел
print()
whs_1.transfer_printers("depart_2", 3)  # Пытаемся передать в Отдел2 принтеров больше (3), чем есть на складе (2)
