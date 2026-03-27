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
        _growth - a float with the ammount which the plant has grown in cm;
        statistics - a StatisticsData variable that keeps track of the
                     plant's statistics
    """
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float = 1) -> None:
        self.name: str = name
        self._growth_rate: float = growth_rate
        self._growth: float = 0
        if height < 0:
            print(f"Tried to create {self.name}"
                  f" from [{self.get_class_name()} class]"
                  f" with negative height - height set to default 0")
            self._height: float = 0
        else:
            self._height = height
        if age < 0:
            print(f"Tried to create {self.name}"
                  f" from [{self.get_class_name()} class]"
                  f" with negative age - age set to default 0")
            self._age: int = 0
        else:
            self._age = age
        self.statistics: Plant.StatisticsData = self.StatisticsData()

    class StatisticsData:
        """
        Represents a group of plant statistics related to certain plant
        operations.
        Attributes:
            _grow_calls - an int that keeps track of how many
                          times the plant has grown;
            _age_calls - an int that keeps track of how many
                         times the plant has aged;
            _show_calls - an int that keeps track of how many
                          times the plant's attributes have been shown
        """
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def get_grow_calls(self) -> int:
            """
            Method that returns _grow_calls
            """
            return self._grow_calls

        def get_age_calls(self) -> int:
            """
            Method that returns _age_calls
            """
            return self._age_calls

        def get_show_calls(self) -> int:
            """
            Method that returns _show_calls
            """
            return self._show_calls

        def add_grow_call(self) -> None:
            """
            Method that increments _grow_calls
            """
            self._grow_calls += 1

        def add_age_call(self) -> None:
            """
            Method that increments _age_calls
            """
            self._age_calls += 1

        def add_show_call(self) -> None:
            """
            Method that increments _show_calls
            """
            self._show_calls += 1

        def display(self) -> None:
            """
            Method that displays the plants statistics:
            _grow_calls, _age_calls and _show_calls
            """
            print(f"Stats: {self.get_grow_calls()} grow,"
                  f" {self.get_age_calls()} age,"
                  f" {self.get_show_calls()} show")

    def grow(self) -> None:
        """
        Method that makes a plant grow by its own growth rate
        """
        self._height += self._growth_rate
        self._growth += self._growth_rate
        self.statistics.add_grow_call()

    def age(self, days: int = 1) -> None:
        """
        Method that makes a plant age by an amount of days
        """
        self._age += days
        self.statistics.add_age_call()

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
        self.statistics.add_show_call()
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def __str__(self) -> str:
        return (f"Current plant: {self.name} "
                f"({self.get_height():.1f}cm, {self.get_age()} days)")

    @staticmethod
    def check_age(age: int) -> bool:
        """
        Static Method that checks if a certain amount of days corresponds to
        at leat a year
        """
        return age > 365

    @classmethod
    def get_class_name(cls) -> str:
        """
        Class Method that returns a class name
        """
        return cls.__name__

    @classmethod
    def anonymous(cls, name: str = "Unknown Plant", height: float = 0,
                  age: int = 0, growth_rate: float = 1) -> "Plant":
        """
        Class Method that instantiates a Plant class object when
        certain arguments are unknown apriori
        """
        return cls(name, height, age, growth_rate)


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

    def set_color(self, color: str) -> None:
        """
        Method that sets the flower's color
        """
        self.color = color

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


class Seed(Flower):
    """
    Represents a subclass of Flower called Seed with certain
    protected attributes and height and age validation.
    If height and age are not valid, sets their
    values to 0
    Attributes:
        name - a string with the flower's name;
        color - a string with the flower's color;
        _height - a float with the flower's height in cm;
        _age - an int with the flower's age in days;
        _growth_rate - a float representing the flower's rate of growth in cm;
        _growth - a float with the ammount which the flower has grown in cm;
        seeds - an int representing the number of seeds present in the,
                flower after blooming
    """
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 1) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self.seeds: int = 0

    def bloom(self) -> None:
        """
        Method that makes the plant bloom
        """
        self.blooming = True
        self.seeds = 42

    def show(self) -> None:
        """
        Method for displaying the flower's name, height in cm, age in days,
        color and if in fact the flower is blooming or not
        """
        super().show()
        print(f"Seeds: {self.seeds}")


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
        self.statistics: Tree.TreeStatisticsData = self.TreeStatisticsData()

    class TreeStatisticsData(Plant.StatisticsData):
        """
        Represents a subclass of StatisticsData for the Tree class.
        Attributes:
            It inherits all the attributes from StatisticsData and adds
            a new one, _shade_calls that keeps track of how many times
            produce_shade has been called.
        """
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def get_shade_calls(self) -> int:
            """
            Method that returns _shade_calls
            """
            return self._shade_calls

        def add_shade_call(self) -> None:
            """
            Method that increments _shade_calls
            """
            self._shade_calls += 1

        def display(self) -> None:
            """
            Method that displays the tree statistics:
            _grow_calls, _age_calls, _show_calls and _shade_calls
            """
            super().display()
            print(f" {self.get_shade_calls()} shade")

    def produce_shade(self) -> None:
        """
        Method that prints the shade produced by the tree
        """
        self.statistics.add_shade_call()
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

    def age(self, days: int = 1) -> None:
        """
        Method that makes a vegetable age by 1 day and increases it's
        nutrional value by 1
        """
        super().age(days)
        self.nutritional_value += days

    def __str__(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}): {self._height}cm"
                f", {self.age} days, {self.harvest_season} harvest, "
                f"{self.nutritional_value} nutritional value")


def display_statistics(plant: Plant) -> None:
    """
    Function that displays a plant's statistics
    """
    print(f"[statistics for {plant.name}]")
    plant.statistics.display()


def main() -> None:
    """
    Main program that instantiates different plant
    objects and tests its methods
    """
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()
    print("=== Flower")
    plant_1 = Flower("Rose", 15, 10, "red", 8)
    plant_1.show()
    display_statistics(plant_1)
    print(f"[asking the {plant_1.name.lower()} to grow and bloom]")
    plant_1.grow()
    plant_1.bloom()
    plant_1.show()
    display_statistics(plant_1)
    print()
    print("=== Tree")
    plant_2 = Tree("Oak", 200, 365, 5)
    plant_2.show()
    display_statistics(plant_2)
    print(f"[asking the {plant_2.name.lower()} to produce shade]")
    plant_2.produce_shade()
    display_statistics(plant_2)
    print()
    print("=== Seed")
    plant_3 = Seed("Sunflower", 80, 45, "yellow", 30)
    plant_3.show()
    print(f"[make {plant_3.name.lower()} grow, age, and bloom]")
    plant_3.grow()
    plant_3.age(20)
    plant_3.bloom()
    plant_3.show()
    display_statistics(plant_3)
    print()
    print("=== Anonymous")
    plant_4 = Plant.anonymous()
    plant_4.show()
    display_statistics(plant_4)


if __name__ == "__main__":
    main()
