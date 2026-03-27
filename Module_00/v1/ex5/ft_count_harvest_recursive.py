def ft_count_harvest_recursive() -> None:
    def helper(day: int, total: int) -> None:
        if day > total:
            print("Harvest time!")
        else:
            print("Day", day)
            helper(day + 1, total)

    days: int = int(input("Days until harvest: "))
    helper(1, days)
