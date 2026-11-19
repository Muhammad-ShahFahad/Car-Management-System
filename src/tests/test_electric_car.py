from car_management.models.electric_car import ElectricCar

tesla = ElectricCar(
    name="Model S",
    make="Tesla",
    model="Plaid",
    horsepower=1020,
    color="Black",
    battery_capacity=100,
    battery_level=50,
)

tesla.start()
tesla.charge(20)
tesla.display_info()
