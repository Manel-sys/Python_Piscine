#!/usr/bin/python3

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["Alice", "Bob", "Dylan", "Charlie",
                          "Dee", "Dennis", "Mac", "Frank",
                          ]

    actions: list[str] = ["run", "eat", "sleep", "eat", "grab",
                          "climb", "move", "swim", "release",
                          "pull", "push", "jump", "laugh"
                          ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[tuple[str, str]]) -> \
                     typing.Generator[tuple[str, str], None, None]:
    while events:
        event: tuple[str, str] = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen: typing.Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        event: tuple[str, str] = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events: list[tuple[str, str]] = []
    for i in range(10):
        events.append(next(gen))
    print(f"Built list of 10 events: {events}")

    gen_2: typing.Generator[tuple[str, str], None, None] = \
        consume_event(events)
    for event in gen_2:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
