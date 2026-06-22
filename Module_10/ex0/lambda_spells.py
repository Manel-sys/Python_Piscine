def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers: list[int] = list(map(lambda mage: mage["power"], mages))

    max_power: int = max(mages, key=lambda mage: mage["power"])["power"]
    min_power: int = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power: float = round(sum(powers) / len(powers), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:

    artifacts: list[dict] = []
    mages: list[dict] = []
    spells: list[str] = []

    try:
        print("Testing artifact sorter...")

        sorted_artifacts: list[dict] = artifact_sorter(artifacts)
        sorted_string: str = ""
        for i in range(len(sorted_artifacts)):
            sorted_string += (f"{sorted_artifacts[i]['name']} "
                              f"({sorted_artifacts[i]['power']} power)")
            if i == 0:
                sorted_string += " comes before "
            elif i > 0 and i < len(sorted_artifacts) - 1:
                sorted_string += " which comes before "
        print(sorted_string)

        print("\nTesting power filter...")
        print(power_filter(mages, 60))
        print("\nTesting spell transformer...")
        print(spell_transformer(spells))
        print("\nTesting mage stats computation...")
        print(mage_stats(mages))
    except (KeyError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}\nCheck the structure of the data being used:"
              "\n(1) artifacts should be a list of dict: {'name': str, "
              "'power': int, 'type': str}"
              "\n(2) mages should be a list of dict: {'name': str,"
              " 'power': int, 'element': str}"
              "\n(3) spells should be a list of str")


if __name__ == "__main__":
    main()
