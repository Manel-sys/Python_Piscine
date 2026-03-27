#!/usr/bin/python3

import sys


def main() -> None:
    total_args: int = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if total_args == 1:
        print("No arguments provided!")
    else:
        args: int = total_args - 1
        print(f"Arguments received: {args}")
        count: int = 1
        for i in sys.argv[1:]:
            print(f"Argument {count}: {i}")
            count += 1
    print(f"Total arguments: {total_args}\n")


if __name__ == "__main__":
    main()
