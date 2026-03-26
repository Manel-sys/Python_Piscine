import sys


def check_format(s: str) -> tuple[str, int]:
    args: list[str] = s.split(":")
    if len(args) != 2:
        raise ValueError(f"Error - invalid parameter '{s}'")
    try:
        return (args[0], int(args[1]))
    except ValueError:
        raise ValueError(f"Quantity error for {args[0]}: invalid literal"
                         f" for int() with base 10: '{args[1]}'")


def parse_args() -> dict[str, int]:
    inv: dict[str, int] = {}

    if len(sys.argv) == 1:
        raise ValueError("No arguments provided. Usage:"
                         " python3 ft_inventory_system.py"
                         " <item1>:<quantity> <item2>:<quantity> ...")
    for s in sys.argv[1:]:
        try:
            arg: tuple[str, int] = check_format(s)
            if arg[0] in inv:
                raise ValueError(f"Redundant item '{arg[0]}' - discarding")
            inv[arg[0]] = arg[1]
        except ValueError as e:
            print(f"{e}")
    return inv


def find_max_min(inv: dict[str, int]) -> None:
    max_key: str = list(inv.keys())[0]
    min_key: str = list(inv.keys())[0]

    for key in inv:
        if inv[key] > inv[max_key]:
            max_key = key
        if inv[key] < inv[min_key]:
            min_key = key
    print(f"Item most abundant: {max_key} with quantity {inv[max_key]}")
    print(f"Item least abundant: {min_key} with quantity {inv[min_key]}")


def update_inv(inv: dict[str, int], new_item: str) -> None:
    try:
        arg: tuple[str, int] = check_format(new_item)
        inv.update([arg])
    except ValueError as e:
        print(f"{e}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    try:
        inv: dict[str, int] = parse_args()
    except ValueError as e:
        print(e)
    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")
    tot_quantity: int = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items: {tot_quantity}")
    for key in inv:
        print(f"Item sword represents"
              f" {round((inv[key] / tot_quantity) * 100, 1)}%")
    find_max_min(inv)
    update_inv(inv, "magic_item:1")
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    main()
