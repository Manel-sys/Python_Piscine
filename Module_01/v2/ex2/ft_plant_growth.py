#!/usr/bin/python3

class Plant:
    """
    Represents a plant, with:
    name - a string with the plant's name;
    height - a float with the plant's height in cm;
    age - an int with the plant's age in days;
    growth_rate - a float representing the plant's rate of growth in cm;
    growth - a float with the ammount which the plant has grown in cm
    """
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name: str = name
        self.height: float = height
        self.plant_age: int = age
        self.growth_rate: float = growth_rate
        self.growth: float = 0

    def show(self) -> None:
        """
        Method for displaying the plant's name, height in cm and age in days
        """
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self) -> None:
        """
        Method that makes a plant grow by its own growth rate
        """
        self.height += self.growth_rate
        self.growth += self.growth_rate

    def age(self) -> None:
        """
        Method that makes a plant age by 1 day
        """
        self.plant_age += 1

    def show_growth(self) -> None:
        """
        Method that shows the amount which the plant has grown in cm
        in a week
        """
        print(f"Growth this week: {round(self.growth)}cm")


def main() -> None:
    """
    Main program that instantiates a plant and simulates its growth
    through 1 week
    """
    plant = Plant("Rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.show()
        plant.age()
        plant.grow()
    plant.show_growth()


if __name__ == "__main__":
    main()
