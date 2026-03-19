class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}): {self.height}cm"
                f", {self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int)\
                                                                    -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade: int = (self.trunk_diameter + 28)
        print(f"{self.name} provides {shade} square meters of shade")

    def __str__(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}): {self.height}cm"
                f", {self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def print_nutrional_value(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def __str__(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}): {self.height}cm"
                f", {self.age} days, {self.harvest_season} harvest")


def main() -> None:
    flower_1 = Flower("Rose", 25, 30, "red")
    flower_2 = Flower("Lily", 15, 15, "yellow")
    tree_1 = Tree("Oak", 500, 1825, 50)
    tree_2 = Tree("Pine Tree", 800, 2000, 60)
    veg_1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    veg_2 = Vegetable("Potato", 60, 80, 'summer', "vitamin C")

    print(flower_1)
    flower_1.bloom()
    print()
    print(flower_2)
    flower_2.bloom()
    print()
    print(tree_1)
    tree_1.produce_shade()
    print()
    print(tree_2)
    tree_2.produce_shade()
    print()
    print(veg_1)
    veg_1.print_nutrional_value()
    print()
    print(veg_2)
    veg_2.print_nutrional_value()


if __name__ == "__main__":
    main()
