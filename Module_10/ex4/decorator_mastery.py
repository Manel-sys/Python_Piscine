from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power: int = kwargs.get("power", args[-1] if args else None)
            if power < min_power or power is None:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for n in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n < max_attempts - 1:
                        print(f"Spell failed, retrying..."
                              f" (attempt {n + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


@retry_spell(3)
def cast_spell(mana: int) -> str:
    if mana < 42:
        raise ValueError("No mana!")
    return "Waaaaaaagh spelled !"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@power_validator(20)
def heal(power: int) -> str:
    return f"Heals for {power} HP"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for char in name:
                if not char.isspace() and not char.isalpha():
                    return False
            return True

        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    try:
        print("\nTesting power validator")
        print(f"Result: {heal(15)}")
        print(f"Result: {heal(42)}")
    except TypeError as e:
        print(e)

    print("\nTesting retrying spell...")
    print(cast_spell(41))
    print(cast_spell(42))

    print("\nTesting MageGuild...")
    mage_guild: MageGuild = MageGuild()
    print(f"{MageGuild.validate_mage_name('Harry Potter')}")
    print(f"{MageGuild.validate_mage_name('42')}")
    print(f"{mage_guild.cast_spell('Psychic Beam', 42)}")
    print(f"{mage_guild.cast_spell('Hydro Pump', 5)}")


if __name__ == "__main__":
    main()
