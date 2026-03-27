#!/usr/bin/python3

import random


def main() -> None:
    players: list[str] = ["Alice", "bob", "Charlie", "dylan",
                          "Emma", "Gregory", "john", "kevin",
                          "Liam"]
    all_capital: list[str] = [p.capitalize() for p in players]
    only_capital: list[str] = [p for p in players if p[0].isupper()]

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_capital}")
    print(f"New list of capitalized names only: {only_capital}\n")

    score_dict: dict[str, int] = {p: random.randint(0, 1000)
                                  for p in all_capital}
    print(f"Score dict: {score_dict}")
    total: int = sum([score_dict[i] for i in score_dict])
    average: float = round(total / len(score_dict), 2)
    print(f"Score average is {average}")

    high_scores: dict[str, int] = {p: score_dict[p] for p in score_dict
                                   if score_dict[p] > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
