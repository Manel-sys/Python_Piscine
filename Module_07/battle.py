from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex0.creature import Creature


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    print("Testing battle")
    base_1: Creature = factory_1.create_base()
    base_2: Creature = factory_2.create_base()

    print(f"{base_1.describe()}\n vs.\n{base_2.describe()}\n fight!")
    print(f"{base_1.attack()}\n{base_2.attack()}")


def main() -> None:
    flame: FlameFactory = FlameFactory()
    aqua: AquaFactory = AquaFactory()

    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    battle(flame, aqua)


if __name__ == "__main__":
    main()
