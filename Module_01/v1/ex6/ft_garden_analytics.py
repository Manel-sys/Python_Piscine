class Plant:
    def __init__(self, name: str, height: int) -> None:
        self._name: str = name
        self._height: int = height
        self._score: int = 20

    def grow(self) -> None:
        self._height += 1
        self._score += 5
        print(f"{self._name} grew 1cm")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> int:
        return self._height

    def get_score(self) -> int:
        return self._score

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    def __str__(self) -> str:
        return f"- {self._name}: {self._height}cm"

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self._color = color
        self._score += 20

    def __str__(self) -> str:
        return f"{super().__str__()}, {self._color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int)\
                                                                 -> None:
        super().__init__(name, height, color)
        self._points = points
        self._score += 20

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self._points}"


class Garden:
    def __init__(self, owner: str) -> None:
        self._owner: str = owner
        self._growth: int = 0
        self._plant_list: list[Plant] = []
        self._plant_types: dict[str, int] = {
                                             "Plant": 0,
                                             "FloweringPlant": 0,
                                             "PrizeFlower": 0
                                            }

    def add_plant(self, plant: Plant) -> None:
        self._plant_list.append(plant)
        self._plant_types[plant.get_class_name()] += 1
        print(f"Added {plant.get_name()} to {self._owner}'s garden")

    def get_owner(self) -> str:
        return self._owner

    def get_plant_list(self) -> list[Plant]:
        return self._plant_list

    def get_growth(self) -> int:
        return self._growth

    def get_plant_types(self) -> dict[str, int]:
        return self._plant_types

    def grow(self) -> None:
        print(f"{self._owner} is helping all plants grow...")
        for plant in self._plant_list:
            plant.grow()
            self._growth += 1
        print()

    def __str__(self) -> str:
        result: str = "Plants in garden:\n"
        for plant in self._plant_list:
            result += plant.__str__() + "\n"
        return result


class GardenManager:
    def __init__(self) -> None:
        self._garden_list: list[Garden] = []
        self._garden_scores: dict[str, int] = {}

    def create_garden_network(self, garden: Garden) -> None:
        self._garden_list.append(garden)

    def report_stats(self) -> None:
        flag: bool = True
        for garden in self._garden_list:
            garden_stats = self.GardenStats(garden)
            garden_stats.compute_score()
            self._garden_scores[garden.get_owner()] = garden_stats.get_score()
            garden_stats.report_garden_stats()
            flag = flag and garden_stats.validate_height()

        print(f"Height validation test: {flag}")
        result: str = "Garden scores - "
        for key, value in self._garden_scores.items():
            result += f"{key}: {value}, "
        result = result[:-2]
        print(result)

        print(f"Total gardens managed: {self._garden_list.__len__()}")

    class GardenStats:
        def __init__(self, garden: Garden) -> None:
            self._garden_score = 0
            self._garden = garden
            self._validation = True

        def validate_height(self) -> bool:
            for plant in self._garden.get_plant_list():
                self._validation = Plant.validate_height(plant.get_height())
            return self._validation

        def compute_score(self) -> None:
            for plant in self._garden.get_plant_list():
                self._garden_score += plant.get_score()

        def get_score(self) -> int:
            return self._garden_score

        def report_garden_stats(self) -> None:
            plant_types: dict[str, int] = self._garden.get_plant_types()
            print(f"=== {self._garden.get_owner()}'s Garden Report ===")
            print(self._garden)
            print(f"Plants added: {self._garden.get_plant_list().__len__()}"
                  f", Total growth: {self._garden.get_growth()}cm")
            print(f"Plant types: {plant_types['Plant']} regular, "
                  f"{plant_types['FloweringPlant']} flowering, "
                  f"{plant_types['PrizeFlower']} prize flowers\n")


def main() -> None:

    print("=== Garden Management System Demo ===\n")
    plant_1 = PrizeFlower("Rose", 15, "Red", 51)
    plant_2 = FloweringPlant("Margarida", 15, "white")
    plant_3 = Plant("Tulip", 9)
    plant_4 = Plant("Oak Tree", 101)

    garden_1 = Garden("Alice")
    garden_1.add_plant(plant_1)
    garden_1.add_plant(plant_2)
    garden_1.add_plant(plant_4)
    garden_2 = Garden("Bob")
    garden_2.add_plant(plant_3)

    print()
    garden_1.grow()
    garden_2.grow()
    garden_manager: GardenManager = GardenManager()
    garden_manager.create_garden_network(garden_1)
    garden_manager.create_garden_network(garden_2)
    garden_manager.report_stats()


if __name__ == "__main__":
    main()
