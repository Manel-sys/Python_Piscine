import sys


def communication_system() -> None:
    try:
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        sys.stdout.flush()
        archivist_id: str = sys.stdin.readline().strip()

        status_rep: str = input("Input Stream active. Enter status report: ")
        print()
        sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}:"
                         f" {status_rep}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication"
                         " channels verified\n")
        print("[STANDARD] Data transmission complete")
    except Exception as e:
        print(f"Error in communication system - {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    communication_system()
    print("\nThree-channel communication test successfull.")


if __name__ == "__main__":
    main()
