import sys
import os
import site


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if not in_virtual_env():
        print("MATRIX STATUS: You're still plugged in\n")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")

    if not in_virtual_env():
        print(f"Current Python: {os.path.realpath(sys.executable)}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\n"
              "the global system.\n")
        print(f"Package installation path:\n{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
