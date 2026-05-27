from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul, gt, lt
from collections.abc import Callable
from typing import Any


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} style jutsu hits {target} for {power} HP"


def spell_reducer(spells: list[int], operations: str) -> int:
    result: int = 0

    if not spells:
        return result

    if operations == "add":
        result = reduce(add, spells)
    elif operations == "multiply":
        result = reduce(mul, spells)
    elif operations == "max":
        result = reduce(lambda x, y: x if gt(x, y) else y, spells)
    elif operations == "min":
        result = reduce(lambda x, y: x if lt(x, y) else y, spells)
    else:
        raise ValueError("Unknown operation in spell_reducer")

    return result


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) \
         -> dict[str, Callable[[str], str]]:
    return {"earth": partial(base_enchantment, 50, "Earth"),
            "wind": partial(base_enchantment, 50, "Wind"),
            "fire": partial(base_enchantment, 50, "Fire")}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(value):
        raise TypeError("Unknown spell type")

    @spell.register(int)
    def _(value) -> str:
        return f"{value} damage"

    @spell.register(str)
    def _(value) -> str:
        return f"{value}"

    @spell.register(list)
    def _(value) -> list[str]:
        return [spell(s) for s in value]

    return spell


def main() -> None:
    spells: list[int] = [10, 20, 30, 40]

    try:
        print("Testing spell reducer...")
        print(f"Sum: {spell_reducer(spells, 'add')}")
        print(f"Product: {spell_reducer(spells, 'multiply')}")
        print(f"Max: {spell_reducer(spells, 'max')}")
        print(f"Min: {spell_reducer(spells, 'min')}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting partial enchanter...")
    for value in partial_enchanter(base_enchantment).values():
        print(f"{value('Target Dummy')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    try:
        dispatcher = spell_dispatcher()
        print("\nTesting spell dispatcher")
        print(f"Damage spell: {dispatcher(42)}")
        print(f"Enchantment: {dispatcher('fireball')}")
        print(f"Multi-cast: {len(dispatcher(['fireball', 42, 'heal']))}")
        print(f"{dispatcher(3.14)}")
    except TypeError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
