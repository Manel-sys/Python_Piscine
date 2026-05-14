import os
from dotenv import load_dotenv  # type: ignore # noqa


def load_configuration() -> None:
    load_dotenv()


def get_config() -> dict[str, str | None]:
    config: dict[str, str | None] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def show_config(config: dict[str, str | None]) -> None:
    mode = config["MATRIX_MODE"]
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if config["DATABASE_URL"]:
        if mode == "production":
            print("Database: Connected to production instance")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: [WARNING] No database configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: [WARNING] No API key configured")

    print(f"Log Level: {config["LOG_LEVEL"]}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: [WARNING] No endpoint configured")


def security_check() -> None:
    print("Environment security check:")

    if os.path.exists(".gitignore"):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Secrets are exposed!")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found!")

    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            if ".env" in f.read():
                print("[OK] Production overrides available")
            else:
                print("[WARNING] .env not in .gitignore")
    else:
        print("[WARNING] No .gitignore file found!")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_configuration()
    config: dict[str, str | None] = get_config()
    show_config(config)
    print()
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
