#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int):
        self.name: str = name
        self.height: int = height


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def check_plant_error(plant: Plant) -> None:
    raise PlantError(f"The {plant.name} plant is wilting!")


def check_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    plant: Plant = Plant("tomato", 15)
    try:
        print("Testing PlantError...")
        check_plant_error(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        check_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        check_plant_error(plant)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    finally:
        print("All custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_errors()


if __name__ == "__main__":
    main()
