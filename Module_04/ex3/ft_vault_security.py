def secure_extraction(file_name: str) -> None:
    print("Initiating secure vault access...")
    try:
        with open(file_name, "r") as file:
            print("Vault connection established with failsafe protocols\n")
            data: str = file.read()
            print(f"SECURE EXTRACTION:\n{data}")
    except OSError as e:
        print(f"Vault connection error - {e}")


def secure_preservation(file_name: str) -> None:
    try:
        with open(file_name, "w") as file:
            print("\nSECURE PRESERVATION:")
            to_preserve: str = "[CLASSIFIED] New security protocols archived"
            file.write(to_preserve)
            print(to_preserve)
    except OSError as e:
        print(f"Vault connection error - {e}")
    print("Vault automatically sealed upon completion")


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    secure_extraction("classified_data.txt")
    secure_preservation("security_protocols.txt")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
