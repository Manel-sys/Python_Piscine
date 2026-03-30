def data_preservation(file_name: str) -> None:
    entries: list[str] = ["[ENTRY 001] New quantum algorithm discovered\n",
                          "[ENTRY 002] Efficiency increased by 347%\n",
                          "[ENTRY 003] Archived by Data Archivist trainee"
                          ]
    try:
        print(f"Initializing new storage unit: {file_name}")
        file = open(file_name, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for entry in entries:
            file.write(entry)
            print(f"{entry}", end="")
        print()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
    except OSError as e:
        print(f"Error - {e}")
    finally:
        if file:
            file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    data_preservation("new_discovery.txt")


if __name__ == "__main__":
    main()
