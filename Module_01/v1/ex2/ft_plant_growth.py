class Plant:
    def __init__(self, name: str, height: int, age: int, growth_rate: int) \
                                                                    -> None:
        self.name: str = name
        self.height: int = height
        self.plant_age: int = age
        self.growth_rate: int = growth_rate
        self.growth: int = 0

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height += self.growth_rate
        self.growth += self.growth_rate

    def age(self) -> None:
        self.plant_age += 1

    def show_growth(self) -> None:
        print(f"Growth this week: {self.growth:+}cm")


def main() -> None:
    plant_list: list[Plant] = [
        Plant("Rose", 25, 30, 1),
        Plant("Sunflower", 80, 45, 3),
        Plant("Cactus", 15, 120, 2),
        ]
    print("=== Day 1 ===")
    for plant in plant_list:
        plant.get_info()
        print()
    for i in range(1, 7):
        for plant in plant_list:
            plant.age()
            plant.grow()
    print("=== Day 7 ===")
    for plant in plant_list:
        plant.get_info()
        plant.show_growth()
        if plant != plant_list[-1]:
            print()


if __name__ == "__main__":
    main()
