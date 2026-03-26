import math


def size_list(lst: list[str]) -> int:
    count: int = 0
    for i in lst:
        count += 1
    return count


def check_format(coord: str) -> list[str]:
    list_coord: list[str] = coord.split(",")
    if size_list(list_coord) != 3:
        raise ValueError("Invalid syntax")
    for i in list_coord:
        try:
            float(i)
        except ValueError:
            raise ValueError(f"Error on parameter '{i}':"
                             f" could not convert string to float: '{i}'")
    return list_coord


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coord: list[str] = check_format(input("Enter new coordinates "
                                                  "as floats in"
                                                  " format 'x,y,z': "))
            return (float(coord[0]), float(coord[1]), float(coord[2]))
        except ValueError as e:
            print(e)


def get_distance(p1: tuple[float, float, float],
                 p2: tuple[float, float, float]) -> float:

    dist: float = math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)
                            + ((p2[2] - p1[2]) ** 2))
    return dist


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    p_1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {p_1}")
    print(f"It includes: X={p_1[0]}, Y={p_1[1]}, Z={p_1[2]}")
    print(f"Distance to center: {round(get_distance((0, 0, 0), p_1), 4)}")

    print("\nGet a second set of coordinates")
    p_2: tuple[float, float, float] = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(get_distance(p_1, p_2), 4)}")


if __name__ == "__main__":
    main()
