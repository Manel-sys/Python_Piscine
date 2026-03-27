class Plant:
    def __init__(self, name: str, height: int):
        self.name: str = name
        self.height: int = height


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str, plant: Plant) -> None:
        super().__init__(message)
        self.plant: Plant = plant


def check_plant_error() -> None:
    plant_1 = Plant("Tomato", 30)
    raise PlantError(f"The {plant_1.name.lower()} plant is wilting!", plant_1)


def check_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    try:
        print("Testing PlantError...")
        check_plant_error()
    except PlantError as e:
        print(f"Caught {e.get_class_name()}: {e}\n")
    try:
        print("Testing WaterError...")
        check_water_error()
    except WaterError as e:
        print(f"Caught {e.get_class_name()}: {e}\n")
    try:
        print("Testing catching all garden errors...")
        check_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    finally:
        print("All custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_errors()


if __name__ == "__main__":
    main()
