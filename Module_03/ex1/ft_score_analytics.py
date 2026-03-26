import sys


def print_statistics(list_scores: list[int]) -> None:
    tot_players = len(list_scores)
    tot_score = sum(list_scores)
    print(f"Scores processed: {list_scores}")
    print(f"Total players: {tot_players}")
    print(f"Total score: {tot_score}")
    print(f"Average score: {tot_score / tot_players:.1f}")
    print(f"High score: {max(list_scores)}")
    print(f"Low score: {min(list_scores)}")
    print(f"Score range: {max(list_scores) - min(list_scores)}")
    print()


def main() -> None:
    print("=== Player Score Analytics ===")
    list_scores: list[int] = []
    for i in sys.argv[1:]:
        try:
            score: int = int(i)
            list_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    try:
        if len(list_scores) == 0:
            raise ValueError("No scores provided. Usage:"
                             " python3 ft_score_analytics.py <score1>"
                             " <score2> ...")
        print_statistics(list_scores)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
