#!/usr/bin/python3

def garden_operations(oper_nbr: int) -> None:
    if oper_nbr == 0:
        nbr: int = int("abc")
        nbr += 1
    elif oper_nbr == 1:
        result: float = 42 / 0
        result += 1
    elif oper_nbr == 2:
        open("/non/existent/file")
    elif oper_nbr == 3:
        result: float = "4" + 2
    else:
        return


def test_error_types() -> None:
    try:
        print("Testing operation 0...")
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    try:
        print("Testing operation 1...")
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        print("Testing operation 2...")
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    try:
        print("Testing operation 3...")
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    try:
        print("Testing operation 4...")
        garden_operations(4)
        print("Operation completed successfully")
    except Exception:
        print("Caught an error")
    try:
        print("Testing multiple errors together...")
        garden_operations(0)
        garden_operations(1)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    finally:
        print("All error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()
