"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle


class Car(Vehicle):
    engine = ''


# объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
def set_engine(self, engine):
    self.engine = engine
    pass
