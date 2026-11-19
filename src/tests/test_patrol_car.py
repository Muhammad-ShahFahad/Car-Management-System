from car_management.models.petrol_car import PetrolCar

car_test = PetrolCar(
    name="Bugatti", make="Bugatti", model="Tourbillon", horsepower=2000, color="Blue"
)

car_test.start()
car_test.stop()
car_test.accelerate()
car_test.brake()


print(car_test)
