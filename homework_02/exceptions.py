

class LowFuelError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class NotEnoughFuel(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class CargoOverload(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
