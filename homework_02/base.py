from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.fuel = fuel
        self.weight = weight
        self.fuel_consumption = fuel_consumption

    # добавьте метод start, который, если ещё не состояние started, проверяет,
    # что топлива больше нуля, и обновляет состояние started,
    # иначе выкидывает исключение exceptions.LowFuelError
    def start(self, ):
        if not self.started:
            try:
                if self.fuel > 0:
                    self.started = True
            except LowFuelError:
                print(LowFuelError())
        else:
            LowFuelError('Low fuel')

    # добавьте метод move, который проверяет, что достаточно топлива для преодоления
    # переданной дистанции, и изменяет количество оставшегося топлива,
    # иначе выкидывает исключение exceptions.NotEnoughFuel
    def move(self, consumption):
        try:
            if self.fuel >= consumption:
                self.fuel -= consumption
        except NotEnoughFuel:
            print(NotEnoughFuel())
