def garden_operations(str_tmp: str) -> None:
    if str_tmp == "ValueError":
        nbr: int = int("abc")
        nbr += 1
    elif str_tmp == "ZeroDivisionError":
        result: float = 42 / 0
        result += 1
    elif str_tmp == "FileNotFoundError":
        open("missing.txt")
    elif str_tmp == "KeyError":
        dic: dict[str, int] = {}
        print(f"{dic['missing_plant']}")


def test_error_types() -> None:
    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")
    try:
        print("Testing multiple errors together...")
        garden_operations("ValueError")
        garden_operations("ZeroDivisionError")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    finally:
        print("All error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_error_types()


if __name__ == "__main__":
    main()
