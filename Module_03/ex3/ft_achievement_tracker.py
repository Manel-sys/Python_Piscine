import random


class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.achievements: set[str] = gen_player_achievements()


def gen_player_achievements() -> set[str]:
    list_achiev: list[str] = ["Crafting Genius", "World Saviour",
                              "Master Explorer", "Collector Supreme",
                              "Untouchable", "Boss Slayer", "Strategist",
                              "Unstoppable", "Speed Runner", "Survivor",
                              "Treasure Hunter", "First Steps", "Sharp Mind"
                              ]
    num = random.randint(1, 13)

    return set(random.sample(list_achiev, num))


def create_union(player: Player, players: list[Player]) -> set[str]:
    set_union: set[str] = set()
    for p in players:
        if p is not player:
            set_union = set_union.union(p.achievements)

    return set_union


def get_missing(players: list[Player]) -> None:
    list_achiev: list[str] = ["Crafting Genius", "World Saviour",
                              "Master Explorer", "Collector Supreme",
                              "Untouchable", "Boss Slayer", "Strategist",
                              "Unstoppable", "Speed Runner", "Survivor",
                              "Treasure Hunter", "First Steps", "Sharp Mind"
                              ]
    set_achiev: set[str] = set(list_achiev)
    for player in players:
        missing: set[str] = set_achiev.difference(player.achievements)
        print(f"{player.name} is missing: {missing}")


def get_differences(players: list[Player]) -> None:
    for player in players:
        diff: set[str] = player.achievements.difference(create_union(player,
                                                                     players))
        print(f"Only {player.name} has: {diff}")


def get_intersection(players: list[Player]) -> set[str]:
    intersect: set[str] = players[0].achievements
    for player in players[1:]:
        intersect = intersect.intersection(player.achievements)
    return intersect


def main() -> None:
    players: list[Player] = [Player("Alice"), Player("Bob"),
                             Player("Charlie"), Player("Dylan")
                             ]

    print("=== Achievement Tracker System ===\n")
    for player in players:
        print(f"Player {player.name}: {player.achievements}")

    common: set[str] = get_intersection(players)
    print(f"\nCommon achievements: {common}\n")
    get_differences(players)
    print()
    get_missing(players)


if __name__ == "__main__":
    main()
