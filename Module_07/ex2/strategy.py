from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       f" for this defensive strategy")

        print(creature.attack())
        print(cast(HealCapability, creature).heal())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       f" for this aggressive strategy")

        print(cast(TransformCapability, creature).transform())
        print(creature.attack())
        print(cast(TransformCapability, creature).revert())
