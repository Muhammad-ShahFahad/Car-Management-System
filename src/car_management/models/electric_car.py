from car_management.models.car import Car

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False

handler = logging.FileHandler(r"D:\OOP_Project\electric_car.log")
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

logger.addHandler(handler)


class ElectricCar(Car):

    def __init__(
        self,
        name: str,
        make: str,
        model: str,
        horsepower: int,
        color: str,
        battery_capacity: float,
        battery_level: float = 100.0,
    ):
        super().__init__(name, make, model, horsepower, color)

        self.battery_capacity = battery_capacity
        self.battery_level = battery_level

    def start(self) -> None:
        if self.battery_level <= 0:
            logger.warning("%s cannot start: battery is empty", self.name)
            print("Battery is empty. Please charge your car.")
            return

        self.is_running = True
        logger.info("%s electric car started", self.name)
        print("Electric car started silently.")

    def charge(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Charging amount must be greater than zero.")

        self.battery_level = min(100.0, self.battery_level + amount)

        logger.info("%s charged. Battery level: %.1f%%", self.name, self.battery_level)

    def display_info(self) -> None:
        super().display_info()

        print(f"Battery Capacity : {self.battery_capacity} kWh")
        print(f"Battery Level    : {self.battery_level}%")
