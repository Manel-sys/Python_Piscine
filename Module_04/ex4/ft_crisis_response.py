def crisis_handler(file_name: str) -> None:
    alert: dict[str, str] = {
        "routine": f"ROUTINE ACCESS: Attempting access to '{file_name}'...",
        "crisis": f"CRISIS ALERT: Attempting access to'{file_name}'...",
                             }
    try:
        with open(file_name, "r") as file:
            print(alert["routine"])
            data: str = file.read()
            print(f"SUCCESS: Archive recovered - ''{data}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(alert["crisis"])
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(alert["crisis"])
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except OSError as e:
        print(alert["crisis"])
        print(f"RESPONSE: Error found - {e}")
        print("STATUS: Crisis handled, system restored\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    crisis_handler(".")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
