class Vehicle:
    """
    Base class for transport
    """

    def __init__(self, brand: str, model: str, horse_power: int):
        """
        Init the onject transport

        brand: Brand of car
        Model: Model of car
        horse_power: amount of horse powers
        """
        self.brand = brand
        self.model = model
        self.horse_power = horse_power

    def start(self) -> str:
        """
        Starts engine
        """
        return f"{self.brand} {self.model}: Engine launched."

    def __str__(self) -> str:
        """
        returns info about vehicle
        """
        return f"{self.brand} {self.model} ({self.horse_power} horse powers)"

    def __repr__(self) -> str:
        """
        representate the vehicle
        """
        return f"Vehicle(brand={self.brand}, model={self.model}, horse powers={self.horse_power})"


class Car(Vehicle):
    """
    common car
    """
    def __init__(self, brand: str, model: str, horse_power: int, cabriolet: bool):
        super().__init__(brand, model, horse_power)
        self.cabriolet = cabriolet

    def start(self) -> str:
        """
        Причина переопределения: На автомобиле обязательно надо пристегиваться.
        """

        return f"{super().start()} Use your seatbelt!"

    def __str__(self) -> str:
        cabriolet_str = "Cabriolet " if self.cabriolet else ""
        return f"{cabriolet_str}{self.brand} {self.model} ({self.horse_power} horse powers)"

    def __repr__(self) -> str:
        cabriolet_str = "Cabriolet " if self.cabriolet else ""
        return f"{cabriolet_str}Car(brand={self.brand}, model={self.model},{self.horse_power} horse powers)"

class Motorcycle(Vehicle):
    """
    class for motorcycle.
    """

    def __init__(self, brand: str, model: str, horse_power: int, has_sidecar: bool) -> None:
        """
        :has_sidecar: (True/False).
        """
        super().__init__(brand, model, horse_power)
        self.has_sidecar = has_sidecar

    def start(self) -> str:
        """
        Причина переопределения: Обязательно надо использовать шлем.

        """
        return f"{super().start()} Use your helmet!"

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.horse_power} horse power), {'with sidecar' if self.has_sidecar else 'without sidecar'}"

    def __repr__(self) -> str:
        return f"Motorcycle(brand={self.brand}, model={self.model}, horse power={self.horse_power}, has_sidecar={self.has_sidecar})"





if __name__ == "__main__":
    car1 = Car("BMW", "Z4", 382, True)
    car2 = Car("Toyota", "Camry", 203, False)
    moto1 = Motorcycle("Harley-Davidson", "Street Glide", 90, False)
    moto2 = Motorcycle("Ural", "Gear Up", 41, True)

    print(car1)
    print(car2)
    print(car1.start())
    print(repr(car1))

    print(moto1)
    print(moto2)
    print(moto1.start())
    print(repr(moto1))
