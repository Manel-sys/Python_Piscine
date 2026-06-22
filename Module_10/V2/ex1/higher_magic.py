from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both arguments must be spells")

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("base_spell must be a spell")

    def amplified(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))

    return amplified


def conditional_caster(condition: Callable,
                       spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("condition must be a callable function that"
                        " returns bool. spell must be a spell")

    def cast(target: str, power: int) -> str:
        if condition(power):
            return spell(target, power)
        return "Spell fizzled"

    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise TypeError("All elements in spells must be spells")

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def main() -> None:

    test_targets: list[str] = ["Dragon", "Goblin", "Wizard", "Knight"]
    test_values: list[int] = [18, 15, 21]
    try:
        print("\nTesting spell combiner...")
        combined_spell = spell_combiner(fireball, shield)
        result = combined_spell(test_targets[0], test_values[0])
        print(f"Combined spell result: {result[0].split(sep='for')[0]},"
              f" {result[1].split(sep='for')[0]}")

        print("\nTesting power amplifier...")
        amplified_spell = power_amplifier(shield, 2)
        result_amplified = amplified_spell(test_targets[1], test_values[1])
        print(f"Original: {test_values[1]}, "
              f"Amplified: {''.join(filter(str.isdigit, result_amplified))}")

        print("\nTesting conditional caster...")
        conditional_spell = conditional_caster(lambda power: power > 20, heal)
        result_conditional_1 = conditional_spell(test_targets[2],
                                                 test_values[2])
        result_conditional_2 = conditional_spell(test_targets[2],
                                                 test_values[1])
        print(f"Testing with power > 20 - {result_conditional_1}")
        print(f"Testing with power < 20 - {result_conditional_2}")

        print("\nTesting spell_sequence...")
        sequence_spell = spell_sequence([heal, fireball, shield])
        result_sequence = sequence_spell(test_targets[3], test_values[0])
        print(result_sequence)

    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
