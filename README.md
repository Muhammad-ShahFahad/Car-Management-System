# Car Management System

A Python-based Car Management System built using Object-Oriented Programming (OOP). It includes an abstract `Car` parent class and two child classes: `PetrolCar` and `ElectricCar`.

The project uses Python logging to track application events and maintain separate log files for different modules.

## Requirements

- Python 3.10 or higher
- pip

## Project Setup

### 1. Navigate to the project directory

```powershell
cd D:\OOP_Project
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the project

```powershell
python -m pip install -e .
```

## Run the Application

Make sure your virtual environment is activated and you are in the project root directory.

Run:

```powershell
python -m car_management.main
```

## Logging

The application uses Python's built-in logging module.

Log files are generated in the `logs/` directory:

| File | Description |
|---|---|
| `car.log` | Logs related to the parent Car class |
| `petrol_car.log` | Logs related to PetrolCar |
| `electric_car.log` | Logs related to ElectricCar |

## Project Structure

```text
OOP_Project/
│
├── src/
│   └── car_management/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── car.py
│       │   ├── petrol_car.py
│       │   └── electric_car.py
│       └── main.py
│
├── tests/
├── logs/
├── pyproject.toml
└── README.md
```