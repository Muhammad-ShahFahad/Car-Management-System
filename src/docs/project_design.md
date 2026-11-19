# Car Management System – Project Design

## 1. Introduction

The Car Management System is a Python application designed using Object-Oriented Programming principles.

The main objective is to create a reusable and maintainable structure for managing different types of cars.

The application uses an abstract parent class named `Car`, while `PetrolCar` and `ElectricCar` provide specialized implementations.

## 2. System Architecture

The application follows a modular structure where each class has its own responsibility.

```text
                  Car (Abstract Class)
                          |
                ---------------------
                |                   |
            PetrolCar           ElectricCar
                |                   |
          Fuel Operations      Battery Operations
                |                   |
           petrol_car.py       electric_car.py
```

### Car – Parent Class

The `Car` class provides common attributes and behaviors shared by all vehicles.

**Common attributes:**

- `name`
- `make`
- `model`
- `horsepower`
- `wheels`
- `year` (if included)
- `color` (if included)
- `is_running`

**Common methods:**

- `start()` – Abstract method that must be implemented by child classes.
- `stop()` – Stops the vehicle.
- `display_info()` – Displays common vehicle information.
- `__str__()` – Returns a readable string representation of the vehicle.

### PetrolCar – Child Class

The `PetrolCar` class inherits common functionality from `Car`.

It implements petrol-specific behavior.

**Responsibilities:**

- Implement the `start()` method.
- Manage fuel-related information.
- Provide refueling functionality.
- Log petrol car operations.

### ElectricCar – Child Class

The `ElectricCar` class inherits common functionality from `Car`.

It implements electric vehicle-specific behavior.

**Responsibilities:**

- Implement the `start()` method.
- Manage battery capacity.
- Track battery percentage.
- Provide charging functionality.
- Log electric car operations.

## 3. Object-Oriented Programming Principles

### Abstraction

The `Car` class inherits from Python's `ABC` class.

The `start()` method is decorated with `@abstractmethod`, requiring concrete child classes to implement their own starting behavior.

### Inheritance

`PetrolCar` and `ElectricCar` inherit common attributes and methods from `Car`.

The `super()` function is used to initialize parent class attributes.

### Encapsulation

Each class manages its own data and related operations.

For example, battery-related functionality belongs to `ElectricCar`, while fuel-related functionality belongs to `PetrolCar`.

### Polymorphism

Both child classes implement the same `start()` method differently.

This allows different vehicle types to respond to the same method call according to their own behavior.

## 4. Logging Architecture

The project uses Python's built-in logging module to track application execution.

Each module creates its own logger using:

```python
logger = logging.getLogger(__name__)
```

Logging levels:

| Level | Purpose |
|---|---|
| DEBUG | Detailed debugging information |
| INFO | Normal application events |
| WARNING | Unexpected situations |
| ERROR | Application errors |
| CRITICAL | Serious application failures |

### Log File Organization

The project maintains separate log files:

- `car.log`
- `petrol_car.log`
- `electric_car.log`

This separation makes it easier to identify which module generated a particular event.

Each logger can use a `FileHandler` to write messages to its respective log file.

## 5. Application Execution Flow

1. The application starts from `main.py`.
2. The required car classes are imported.
3. A specific car object is created.
4. The parent constructor initializes common attributes.
5. The child class implements its specific behavior.
6. Methods such as `start()`, `stop()`, and `display_info()` are called.
7. Logging records the relevant application events.

## 6. Design Goals

The project follows these software design goals:

- **Modularity:** Separate classes and modules according to their responsibilities.
- **Reusability:** Common functionality is implemented in the parent class.
- **Maintainability:** Changes to common functionality can be made centrally.
- **Extensibility:** New vehicle types can be added through additional child classes.
- **Readability:** Type hints, meaningful names, and logging improve code clarity.

## 7. Future Enhancements

Possible future improvements include:

- Vehicle inventory management.
- Car registration and identification.
- Fuel consumption calculations.
- Electric vehicle range calculations.
- Database integration.
- Improved validation and exception handling.
- Automated testing with pytest.

## 8. Conclusion

The Car Management System demonstrates how OOP principles can be used to organize a Python application.

The project provides a foundation for learning abstraction, inheritance, encapsulation, polymorphism, modular project structure, and application logging.