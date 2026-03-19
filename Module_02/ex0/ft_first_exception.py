def check_temperature(temp_str: str) -> int:
    try:
        nbr: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number\n")
    if nbr > 40:
        raise ValueError(f"Error: {nbr}°C is too hot"
                         f" for plants (max 40°C)\n")
    elif nbr < 0:
        raise ValueError(f"Error: {nbr}°C is too cold"
                         f" for plants (min 0°C)\n")
    print(f"Temperature {nbr}°C is perfect for plants!\n")
    return nbr


def test_temperature_input() -> int | None:
    nbr: int | None = None

    try:
        print("Testing temperature: 25")
        nbr = check_temperature("25")
    except ValueError as e:
        print(e)
    try:
        print("Testing temperature: abc")
        nbr = check_temperature("abc")
    except ValueError as e:
        print(e)
    try:
        print("Testing temperature: 100")
        nbr = check_temperature("100")
    except ValueError as e:
        print(e)
    try:
        print("Testing temperature: -50")
        nbr = check_temperature("-50")
    except ValueError as e:
        print(e)
    finally:
        print("All tests completed - program didn't crash!")
    return nbr


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()


if __name__ == "__main__":
    main()
