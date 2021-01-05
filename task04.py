# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"The car {self.name} has started.")

    def stop(self):
        print(f"The car {self.name} has stopped.")

    def turn(self, direction):
        print(f"The car {self.name} has turned to the {direction}.")

    def show_speed(self):
        print(f"Your current speed is: {self.speed}.")


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Your current speed is: {self.speed}.")
            print("You have exceeded the speed limit!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Your current speed is: {self.speed}")
            print("You have exceeded the speed limit!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


town_car_1 = TownCar(70, "blue", "Peugeot")
town_car_1.go()
print(f"TownCar_1: {town_car_1.color} {town_car_1.name}, speed {town_car_1.speed}, "
      f"the car is a police car: {town_car_1.is_police}.")
town_car_1.show_speed()
town_car_1.turn("right")
town_car_1.stop()
print()
sport_car_1 = SportCar(90, "grey", "Porsche")
sport_car_1.go()
print(f"SportCar_1: {sport_car_1.color} {sport_car_1.name}, speed {sport_car_1.speed}, "
      f"the car is a police car: {sport_car_1.is_police}.")
sport_car_1.show_speed()
sport_car_1.turn("left")
sport_car_1.stop()
print()
work_car_1 = WorkCar(50, "yellow", "Komatsu")
work_car_1.go()
print(f"WorkCar_1: {work_car_1.color} {work_car_1.name}, speed {work_car_1.speed}, "
      f"the car is a police car: {work_car_1.is_police}.")
work_car_1.show_speed()
work_car_1.turn("right")
work_car_1.stop()
print()
police_car_1 = PoliceCar(80, "black", "Ford")
police_car_1.go()
print(f"PoliceCar_1: {police_car_1.color} {police_car_1.name}, speed {police_car_1.speed}, "
      f"the car is a police car: {police_car_1.is_police}.")
police_car_1.show_speed()
police_car_1.turn("left")
police_car_1.stop()
