class Plant:
    """
    Represents a plant with certain protected attributes
    and height and age validation. If height and age are not valid, sets their
    values to 0
    Attributes:
        name - a string with the plant's name;
        _height - a float with the plant's height in cm;
        _age - an int with the plant's age in days;
        _growth_rate - a float representing the plant's rate of growth in cm;
        _growth - a float with the ammount which the plant has grown in cm
    """
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float = 1) -> None:
        self.name: str = name
        self._growth_rate: float = growth_rate
        self._growth: float = 0
        if height < 0:
            self._height: float = 0
        else:
            self._height = height
        if age < 0:
            self._age: int = 0
        else:
            self._age = age
        print("Plant created: ", end="")
        self.show()

    def grow(self) -> None:
        """
        Method that makes a plant grow by its own growth rate
        """
        self._height += self._growth_rate
        self._growth += self._growth_rate

    def age(self) -> None:
        """
        Method that makes a plant age by 1 day
        """
        self._age += 1

    def show_growth(self) -> None:
        """
        Method that shows the amount which the plant has grown in cm
        """
        print(f"Growth: {round(self._growth)}cm")

    def set_height(self, height: float) -> None:
        """
        Method that sets the plant's height to a new value
        (only values >= 0) are accepted. If an invalid value is provided,
        prints an error message
        """
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        """
        Method that sets the plant's age to a new value
        (only values >= 0) are accepted. If an invalid value is provided,
        prints an error message
        """
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")

    def get_height(self) -> float:
        """
        Method that returns the protected _height attribute
        """
        return self._height

    def get_age(self) -> int:
        """
        Method that returns the protected _age attribute
        """
        return self._age

    def show(self) -> None:
        """
        Method for displaying the plant's name, height in cm and age in days
        """
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def __str__(self) -> str:
        return (f"Current plant: {self.name} "
                f"({self.get_height():.1f}cm, {self.get_age()} days)")


def main() -> None:
    """
    Main program that instantiates a plant and tests its methods
    """
    print("=== Garden Security System ===")
    plant_1 = Plant("Rose", 15, 10)
    print()
    plant_1.set_height(25)
    plant_1.set_age(30)
    print()
    plant_1.set_height(-15)
    plant_1.set_age(-1)
    print()
    print("Current state: ", end="")
    plant_1.show()


if __name__ == "__main__":
    main()
