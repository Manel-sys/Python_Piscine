from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_output: str = ",".join(d[1] for d in data)
        print("CSV Output:")
        print(csv_output)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        entries: list[str] = [f'"item_{i}": "{s}"' for i, s in data]
        json_output: str = "{" + ", ".join(entries) + "}"
        print("JSON Output:")
        print(json_output)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        limit: int
        for proc in self.processors:
            outputs: list[tuple[int, str]] = []
            limit = nb
            if nb > len(proc.data):
                limit = len(proc.data)
            for i in range(0, limit):
                outputs.append(proc.output())
            if outputs:
                plugin.process_output(outputs)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

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

    data_batch_1: list[Any] = [
                    21,
                    ["I love AI", "LLMs are wonderful", "Stay healthy"],
                    [{"log_level": "ERROR",
                      "log_message": "500 server crash"},
                     {"log_level": "NOTICE",
                      "log_message": "Certificate expires in 10 days"}],
                    [32, 42, 64, 84, 128, 168],
                    "World hello"
                            ]

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    print(f"Send first batch of data on stream: {data_batch}")
    data_stream.process_stream(data_batch)

    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())

    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()

    print(f"\nSend another batch of data: {data_batch_1}")
    data_stream.process_stream(data_batch_1)

    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())

    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
