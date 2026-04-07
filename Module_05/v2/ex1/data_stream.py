from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[tuple[int, str]] = []
        self.proc_nbr: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise IndexError(f"Error in {self.__class__.__name__}.output() -"
                             f" No data available in processor")
        return self.data.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if isinstance(data, (int, float)):
            self.data.append((self.proc_nbr, str(data)))
            self.proc_nbr += 1
        elif isinstance(data, list) and all(isinstance(x, (int, float)) for x
                                            in data):
            for x in data:
                self.data.append((self.proc_nbr, str(x)))
                self.proc_nbr += 1
        else:
            raise TypeError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if isinstance(data, str):
            self.data.append((self.proc_nbr, data))
            self.proc_nbr += 1
        elif isinstance(data, list) and all(isinstance(x, str) for x
                                            in data):
            for x in data:
                self.data.append((self.proc_nbr, x))
                self.proc_nbr += 1
        else:
            raise TypeError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        valid_keys: list[str] = ["log_level", "log_message"]

        if isinstance(data, dict):
            return (list(data.keys()) == valid_keys and
                    all(isinstance(k, str) and isinstance(v, str)
                        for k, v in data.items())
                    )
        elif isinstance(data, list):
            for d in data:
                if not (isinstance(d, dict) and list(d.keys()) == valid_keys
                        and all(isinstance(k, str) and isinstance(v, str)
                                for k, v in d.items())):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        if isinstance(data, dict):
            self.data.append((self.proc_nbr,
                              f"{data['log_level']}: {data['log_message']}"))
            self.proc_nbr += 1
        elif isinstance(data, list):
            for d in data:
                self.data.append((self.proc_nbr,
                                  f"{d['log_level']}: {d['log_message']}"))
                self.proc_nbr += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise TypeError(f"Error in register_process: expected proc to be a"
                            f" DataProcessor got {proc.__class__.__name__}")
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        if not isinstance(stream, list):
            raise TypeError(f"Error in process_stream: expected stream"
                            f" to be a list got {stream.__class__.__name__}")
        handled: bool
        for data in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process element"
                      f" in stream: {data}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name: str = proc.__class__.__name__.replace("Processor",
                                                        " Processor")
            print(f"{name}: total {proc.proc_nbr} items "
                  f"processed, remaining {len(proc.data)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    data_stream: DataStream = DataStream()
    data_batch: list[Any] = [
                    "Hello world",
                    [3.14, -1, 2.71],
                    [{"log_level": "WARNING",
                      "log_message": "Telnet access! Use ssh instead"},
                     {"log_level": "INFO",
                      "log_message": "User wil is connected"}],
                    42,
                    ["Hi", "five"],
                    ]

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(NumericProcessor())

    print(f"Send first batch of data on stream: {data_batch}")
    data_stream.process_stream(data_batch)
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nRegistering other data processors\n")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    print("Send the same batch again")
    data_stream.process_stream(data_batch)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nConsume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    for i in range(0, 3):
        data_stream.processors[0].output()
    for i in range(0, 2):
        data_stream.processors[1].output()
    data_stream.processors[2].output()

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
