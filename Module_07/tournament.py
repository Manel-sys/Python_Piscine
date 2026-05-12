from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, DefensiveStrategy)
from ex2 import InvalidStrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    creatures: list[tuple[Creature, BattleStrategy]] = []

    for factory, strategy in opponents:
        creatures.append((factory.create_base(), strategy))

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            c1, s1 = creatures[i]
            c2, s2 = creatures[j]

            print("* Battle *")
            print(c1.describe())
            print(" vs")
            print(c2.describe())
            print(" now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
                print()

            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}\n")
                return


def main() -> None:

    print("Tournament 0 (basic)")
    opponents: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        ]

    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(opponents)

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents)

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    battle(opponents)


if __name__ == "__main__":
    main()
