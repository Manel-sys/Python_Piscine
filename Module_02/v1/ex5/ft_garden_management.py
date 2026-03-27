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
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str, height: int, water: int = 1, sun: int = 8):
        self.name: str = name
        self.height: int = height
        self.water: int = water
        self.sun: int = sun

    @staticmethod
    def check_name(name: str) -> bool:
        if name == "":
            return False
        return True

    @staticmethod
    def check_height(height: int) -> bool:
        if height < 0:
            return False
        return True

    def check_water(self) -> None:
        if self.water > 10:
            raise WaterError(f"Water level {self.water}"
                             f" is too high (max 10)")
        elif self.water < 1:
            raise WaterError(f"Water level {self.water} is too low (min 1)")

    def check_sunlight(self) -> None:
        if self.sun > 12:
            raise PlantError(f"Sunlight hours {self.sun}"
                             f" is too high (max 12)")
        elif self.sun < 2:
            raise PlantError(f"Sunlight hours {self.sun}"
                             f" is too low (min 2)")


class GardenManager:
    def __init__(self, water_lvl: int = 35) -> None:
        self.plants_list: list[Plant] = []
        self.water_tank_lvl: int = water_lvl

    def check_water_lvl(self) -> None:
        if (self.water_tank_lvl <= 0):
            raise GardenError("Not enough water in tank")
        print("There is still some water left in the tank")

    def add_plant(self, name: str, height: int, water: int = 1,
                  sun: int = 8) -> None:
        try:
            if not Plant.check_name(name):
                raise PlantError("Plant name cannot be empty!")
            if not Plant.check_height(height):
                raise PlantError(f"Plant height [{height}cm]"
                                 f" not valid (min 0cm)")
            self.plants_list.append(Plant(name, height, water, sun))
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        i: int = 0
        print("Opening watering system")
        try:
            while i < self.plants_list.__len__():
                plant = self.plants_list[i]
                if self.water_tank_lvl >= 1:
                    self.water_tank_lvl -= 1
                    plant.water += 1
                    print(f"Watering {self.plants_list[i].name} - success")
                    i += 1
                else:
                    raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught {e.get_class_name()}: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        i: int = 0
        while i < self.plants_list.__len__():
            plant = self.plants_list[i]
            try:
                plant.check_water()
                plant.check_sunlight()
                print(f"{plant.name}: healthy (water: {plant.water},"
                      f" sun: {plant.sun})")
            except (WaterError, PlantError) as e:
                print(f"Error checking {plant.name}: {e}")
            i += 1


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    g_m = GardenManager(water_lvl=2)
    g_m.add_plant("tomato", 10, 4)
    g_m.add_plant("lettuce", 25, 14)
    g_m.add_plant("", 30)

    print("\nWatering plants...")
    g_m.water_plants()
    print("\nChecking plant health...")
    g_m.check_plant_health()
    print("\nTesting error recovery...")
    try:
        g_m.check_water_lvl()
    except GardenError as e:
        print(f"Caught {e.get_class_name()}: {e}")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
