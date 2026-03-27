class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Invalid operation attempted: "
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Invalid operation attempted: "
                  f"age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {self.get_age()} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def __str__(self) -> str:
        return (f"Current plant: {self.name} "
                f"({self.get_height()}cm, {self.get_age()} days)")


def main() -> None:
    print("=== Garden Security System ===")
    plant_1 = SecurePlant("Rose", -25, 30)
    print()
    plant_1.set_height(-5)
    print()
    print(plant_1)


if __name__ == "__main__":
    main()
