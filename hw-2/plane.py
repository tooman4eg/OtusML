"""
создайте класс `Plane`, наследник `Vehicle`
"""
from vehicle import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0


def __init__(self, max_cargo):
    self.max_cargo = max_cargo


def load_cargo(self, cargo):
    try:
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo

    except CargoOverload:
        CargoOverload('Cargo overload')


def remove_all_cargo(self):
    print(self.cargo)
    self.cargo = 0
