def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         f" is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         f" is too low (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    count: int = 0
    print("Testing good values...")
    try:
        count += 1
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing empty plant name...")
    try:
        count += 1
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing bad water level...")
    try:
        count += 1
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing bad sunlight hours...")
    try:
        count += 1
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    if count == 4:
        print("\nAll error raising tests completed!")


def main() -> None:
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()


if __name__ == "__main__":
    main()
