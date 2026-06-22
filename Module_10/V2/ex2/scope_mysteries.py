from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    i: int = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power: int = initial_power

    def accumulator(to_add: int) -> int:
        nonlocal total_power
        total_power += to_add
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return factory


def memory_vault() -> dict[str, Callable]:
    memory: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        memory[key] = value

    def recall(key: Any) -> Any:
        if key in memory.keys():
            return memory[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    spell_accumulate = spell_accumulator(100)
    print(f"Base 100, add 20: {spell_accumulate(20)}")
    print(f"Base 100, add 30: {spell_accumulate(30)}")

    print("\nTesting enchantment factory...")
    fire_factory = enchantment_factory("Flaming")
    ice_factory = enchantment_factory("Frozen")
    print(f"{fire_factory('Sword')}")
    print(f"{ice_factory('Shield')}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
