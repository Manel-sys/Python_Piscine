class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    plant_list: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    count: int = 0
    for plant in plant_list:
        count += 1

    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
