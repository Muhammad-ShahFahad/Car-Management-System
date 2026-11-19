from car_management.models.car import Car
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False

handler = logging.FileHandler(r"D:\OOP_Project\pertrol_car.log")
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

logger.addHandler(handler)


class PetrolCar(Car):
    def __init__(self, name, make, model, horsepower, color):
        super().__init__(name, make, model, horsepower, color)

    def start(self):
        logger.info(f"{self.name} Started.")

    def stop(self):
        logger.info("%s stoped", self.name)

    def accelerate(self):
        logger.info(f"The {self.name} is accelerating.")

    def brake(self):
        logger.info(f"The {self.name} is stopping")

    def display_info(self) -> None:
        logger.info("Displaying car information")
