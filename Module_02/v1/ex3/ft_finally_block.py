class Plant:
    def __init__(self, name: str) -> None:
        self.name: str = name

    @staticmethod
    def check_name(name: str) -> bool:
        if not name.isalpha() or name == "None":
            return False
        return True


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def water_plants(plant_list: list[Plant]) -> None:
    print("Opening watering system")
    i: int = 0
    flag: bool = True
    try:
        while i < plant_list.__len__():
            plant = plant_list[i]
            if not Plant.check_name(plant.name):
                raise PlantError(f"Cannot water {plant.name}"
                                 f" - invalid plant!")
            print(f"Watering {plant.name}")
            i += 1
    except PlantError as e:
        print(f"Error: {e}")
        flag = False
    finally:
        print("Closing watering system (cleanup)")
    if flag:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    print("Testing normal watering...")
    plant_1 = Plant("tomato")
    plant_2 = Plant("lettuce")
    plant_3 = Plant("carrots")

    list_plants: list[Plant] = [plant_1,
                                plant_2,
                                plant_3,
                                ]
    water_plants(list_plants)
    print("\nTesting with error...")
    plant_4 = Plant("None")
    list_plants.clear()
    list_plants.extend([plant_1,
                        plant_4,
                        plant_2,
                        plant_3,
                        ])
    water_plants(list_plants)


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
