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


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate("Hello")}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except Exception as e:
        print(f" Got exception: {e}")
    print(" Processing data: [1, 2, 3, 4, 5]")
    try:
        num_proc.ingest([1, 2, 3, 4, 5])
    except Exception as e:
        print(f" Got exception: {e}")  
    try:
        print(" Extracting 3 values...")
        for i in range(0, 3):
            result: tuple[int, str] = num_proc.output()
            print(f" Numeric value {result[0]}: {result[1]}")
    except Exception as e:
        print(f" Got exception: {e}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f" Trying to validate input '42': {text_proc.validate(42)}")
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    try:
        text_proc.ingest(["Hello", "Nexus", "World"])
    except Exception as e:
        print(f" Got exception: {e}")
    try:
        print(" Extracting 1 value...")
        for i in range(0, 1):
            result = text_proc.output()
            print(f" Text value {result[0]}: {result[1]}")
    except Exception as e:
        print(f" Got exception: {e}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_proc.validate("Hello")}")
    data: Any = [
                {"log_level": "NOTICE", "log_message": "Connection to server"},
                {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
                ]
    print(f" Processing data: {data}")
    try:
        log_proc.ingest(data)
    except Exception as e:
        print(f" Got exception: {e}")
    try:
        print(" Extracting 2 values...")
        for i in range(0, 2):
            result = log_proc.output()
            print(f" Log entry {result[0]}: {result[1]}")
    except Exception as e:
        print(f" Got exception: {e}")


if __name__ == "__main__":
    main()
