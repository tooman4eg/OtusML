"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, *args, **kwargs):
        print('LowFuelError')


pass


class NotEnoughFuel(Exception):
    def __init__(self, *args, **kwargs):
        print('LowFuelError')


pass


class CargoOverload(Exception):
    def __init__(self, *args, **kwargs):
        print('LowFuelError')


pass
