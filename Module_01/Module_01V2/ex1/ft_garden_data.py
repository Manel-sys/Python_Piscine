#!/usr/bin/python3

class Plant:
    """
    Represents a plant with a name, height and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        """
        Displays the plant's attributes to stdout
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """
    Main program that instantiates 3 different plants and displays
    their attributes.
    """
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant_1.show()
    plant_2.show()
    plant_3.show()


if __name__ == "__main__":
    main()
