def data_recovery(file_name: str) -> None:
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name, "r")
        print("Connection established...\n")
        data: str = file.read()
        print(f"RECOVERED DATA:\n{data}")
        print("\nData recovery complete. Storage unit disconnected.")
    except OSError:
        print("ERROR: Storage vault not found - No connection established."
              "Exiting...")
    finally:
        if file:
            file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    data_recovery("ancient_fragment.txt")


if __name__ == "__main__":
    main()
