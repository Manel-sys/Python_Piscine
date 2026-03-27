def input_temperature(temp_str: str) -> int:
    try:
        nbr: int = int(temp_str)
    except ValueError:
        raise
    print(f"Temperature is now {nbr}°C\n")
    return nbr


def test_temperature() -> int | None:
    nbr: int | None = None

    try:
        print("Input data is '25'")
        nbr = input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        print("Input data is 'abc'")
        nbr = input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    finally:
        print("All tests completed - program didn't crash!")
    return nbr


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
