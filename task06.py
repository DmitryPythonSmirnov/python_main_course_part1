"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class Warehouse:
    whs_equip_qty = {"printers": 0, "scanners": 0, "copiers": 0}  # Оборудование на складе
    depart_1 = {"printers": 0, "scanners": 0, "copiers": 0}  # Оборудование в Отделе1
    depart_2 = {"printers": 0, "scanners": 0, "copiers": 0}  # Оборудование в Отделе2

    # Прием принтеров на склад
    @classmethod
    def get_printers(cls, num):
        if type(num) == int:
            cls.whs_equip_qty["printers"] += num
            print(f"Получили на склад {num} принтеров.")
        else:
            print("Передано не число.")

    # Прием сканеров на склад
    @classmethod
    def get_scanner(cls, num):
        if type(num) == int:
            cls.whs_equip_qty["scanners"] += num
            print(f"Получили на склад {num} сканеров.")
        else:
            print("Передано не число.")

    # Прием копиров на склад
    @classmethod
    def get_copier(cls, num):
        if type(num) == int:
            cls.whs_equip_qty["copiers"] += num
            print(f"Получили на склад {num} копиров.")
        else:
            print("Передано не число.")

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
whs_1.get_printers("1")
print()
whs_1.get_printers(1)
