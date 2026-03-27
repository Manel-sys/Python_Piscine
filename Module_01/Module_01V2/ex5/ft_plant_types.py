#!/usr/bin/python3

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
            print(f"Tried to create {self.name}"
                  f" with negative height - height set to default 0")
            self._height: float = 0
        else:
            self._height = height
        if age < 0:
            print(f"Tried to create {self.name}"
                  f" with negative age - age set to default 0")
            self._age: int = 0
        else:
            self._age = age

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


class Flower(Plant):
    """
    Represents a subclass of Plant called Flower with certain
    protected attributes and height and age validation.
    If height and age are not valid, sets their
    values to 0
    Attributes:
        name - a string with the flower's name;
        color - a string with the flower's color;
        _height - a float with the flower's height in cm;
        _age - an int with the flower's age in days;
        _growth_rate - a float representing the flower's rate of growth in cm;
        _growth - a float with the ammount which the flower has grown in cm
    """
    def __init__(self, name: str, height: float,
                 age: int, color: str, growth_rate: float = 1) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color: str = color
        self.blooming: bool = False

    def bloom(self) -> None:
        """
        Method that makes the flower bloom
        """
        self.blooming = True

    def show(self) -> None:
        """
        Method for displaying the flower's name, height in cm, age in days,
        color and if in fact the flower is blooming or not
        """
        super().show()
        print(f" Color: {self.color}")
        if not self.blooming:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def __str__(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}):"
                f" {self._height:.1f}cm"
                f", {self.age} days, {self.color} color")


class Tree(Plant):
    """
    Represents a subclass of Plant called Tree with certain
    protected attributes and height and age validation.
    If height and age are not valid, sets their values to 0
    Attributes:
        name - a string with the tree's name;
        _height - a float with the tree's height in cm;
        _age - an int with the tree's age in days;
        _growth_rate - a float representing the tree's rate of growth in cm;
        _growth - a float with the ammount which the tree has grown in cm;
        trunk_diameter - a float with the tree's trunk diameter in cm
    """
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth_rate: float = 1) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        """
        Method that prints the shade produced by the tree
        """
        print(f"{self.__class__.__name__} {self.name} now produces a shade of "
              f"{self.get_height():.1f}cm long and"
              f" {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        """
        Method for displaying the tree's name, height in cm, age in days
        and trunk diameter in cm
        """
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def __str__(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}): {self._height}cm"
                f", {self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a subclass of Plant called Vegetable with certain
    protected attributes and height and age validation.
    If height and age are not valid, sets their values to 0
    Attributes:
        name - a string with the tree's name;
        _height - a float with the tree's height in cm;
        _age - an int with the tree's age in days;
        _growth_rate - a float representing the tree's rate of growth in cm;
        _growth - a float with the ammount which the tree has grown in cm;
        harvest_season - a string with the vegetable's season to harvest;
        nutritional_value - an int with the vegetable's nutrional value
    """
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int,
                 growth_rate: float = 1) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def show(self) -> None:
        """
        Method for displaying the vegetable's name, height in cm,
        age in days, harvest season and nutrional value
        """
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        """
        Method that makes a vegetable age by 1 day and increases it's
        nutrional value by 1
        """
        super().age()
        self.nutritional_value += 1

    def __str__(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}): {self._height}cm"
                f", {self.age} days, {self.harvest_season} harvest, "
                f"{self.nutritional_value} nutritional value")


def main() -> None:
    """
    Main program that instantiates different types of plants and
    tests their methods
    """
    flower_1 = Flower("Rose", 15, 10, "red")
    tree_1 = Tree("Oak", 200, 365, 5)
    veg_1 = Vegetable("Tomato", 5, 10, "April", 0, 2.1)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower_1.show()
    print(f"[asking the {flower_1.name.lower()} to bloom]")
    flower_1.bloom()
    flower_1.show()
    print()
    print("=== Tree")
    tree_1.show()
    tree_1.produce_shade()
    print()
    print("=== Vegetable")
    veg_1.show()
    for i in range(0, 20):
        veg_1.age()
        veg_1.grow()
    veg_1.show()
    print()


if __name__ == "__main__":
    main()
