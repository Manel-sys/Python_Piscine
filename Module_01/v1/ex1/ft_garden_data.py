class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(plant_1)
    print(plant_2)
    print(plant_3)


if __name__ == "__main__":
    main()
