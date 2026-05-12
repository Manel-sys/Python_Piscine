from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex0.creature import Creature
from typing import cast


def main() -> None:
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()

    base_healing: Creature = healing_factory.create_base()
    evolved_healing: Creature = healing_factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    print(base_healing.describe())
    print(base_healing.attack())
    print(cast(HealCapability, base_healing).heal())

    print(" evolved:")
    print(evolved_healing.describe())
    print(evolved_healing.attack())
    print(cast(HealCapability, evolved_healing).heal())

    transforming_factory: TransformCreatureFactory = TransformCreatureFactory()

    base_transform: Creature = transforming_factory.create_base()
    evolved_transform: Creature = transforming_factory.create_evolved()

    print("\nTesting Creature with transform capability")
    print(" base:")
    print(base_transform.describe())
    print(base_transform.attack())
    print(cast(TransformCapability, base_transform).transform())
    print(base_transform.attack())
    print(cast(TransformCapability, base_transform).revert())

    print(" evolved:")
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(cast(TransformCapability, evolved_transform).transform())
    print(evolved_transform.attack())
    print(cast(TransformCapability, evolved_transform).revert())


if __name__ == "__main__":
    main()
