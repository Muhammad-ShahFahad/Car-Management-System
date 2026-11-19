from abc import ABC, abstractmethod
import logging
from logging import INFO, DEBUG, ERROR, WARNING

logging.basicConfig(
    level=INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=r"D:\OOP_Project\car.log",
)

logger = logging.getLogger(__name__)


class Car(ABC):
    def __init__(self, name: str, make: int, model: str, color: str, horsepower: int):
        self.name = name
        self.make = make
        self.model = model
        self.horsepower = horsepower
        self.wheels = 4
        self.color = color

    @abstractmethod
    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def accelerate(self) -> None:
        pass

    def brake(self) -> None:
        pass

    def display_info(self) -> None:
        logger.info("Displaying car information")

        print("\n========== CAR INFORMATION ==========")
        print(f"Name        : {self.name}")
        print(f"Make        : {self.make}")
        print(f"Model       : {self.model}")
        print(f"Horsepower  : {self.horsepower} HP")
        print(f"Wheels      : {self.wheels}")
        print(f"Color       : {self.color}")
        print(f"Running     : {self.is_running}")
        print("=====================================")

    def __str__(self):
        logger.info("__str__ method called")
        return f"Name : {self.name}, Make : {self.make}, Model : {self.model}, Horsepower : {self.horsepower}, Color : {self.color} Wheels : {self.wheels}"
