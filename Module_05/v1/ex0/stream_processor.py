from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:

        if not self.validate(data):
            raise ValueError("Validation: [ERROR] Invalid data - "
                             "expected a non-empty list of numbers")

        nums: list[float] = [float(value) for value in data]
        count: int = len(nums)
        total: float = sum(nums)
        if total.is_integer():
            total = int(total)
        avg: float = total / count

        return f"Processed {count} numeric values, sum={total}, avg={avg:.1f}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        try:
            for value in data:
                float(value)
            return True
        except (ValueError, TypeError):
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Validation: [ERROR] Invalid data - "
                             "expected a string")

        words: int = len(data.split())
        chars: int = len(data)
        return f"Processed text: {chars} characters, {words} words"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        log_lvls: list[str] = ["ERROR", "INFO", "WARNING",
                               "DEBUG", "CRITICAL"]

        if isinstance(data, str):
            if data.split(":")[0] in log_lvls:
                return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Validation: [ERROR] Invalid data - "
                             "expected a string starting with a log level"
                             " (ERROR, INFO, WARNING, DEBUG, CRITICAL)")

        log_lvl: str = data.split(":")[0]
        message: str = " ".join(data.split(":")[1:]).strip()
        tag: str = log_lvl
        if log_lvl in ["ERROR", "CRITICAL"]:
            tag = "ALERT"
        return f"[{tag}] {log_lvl} level detected: {message}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def run_processor(processor: DataProcessor, data: Any) -> None:
    print(f"Processing data: {data}")
    try:
        result: str = processor.process(data)
        print(processor.format_output(result))
    except ValueError as e:
        print(f"{e}")
    print()


def polymorphic_demo() -> None:
    test_cases: list[tuple[DataProcessor, Any]] = [
                                    (NumericProcessor(), [1, 2, 3]),
                                    (TextProcessor(), "System ready"),
                                    (LogProcessor(), "INFO: System ready"),
                                    ]
    print("Processing multiple data types through same interface...")
    for i in range(0, 3):
        result: str = test_cases[i][0].process(test_cases[i][1])
        print(f"Result {i+1}: {result}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    data: Any
    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    if NumericProcessor().validate(data):
        print("Validation: Numeric data verified")
    run_processor(NumericProcessor(), data)

    print("Initializing Text Processor...")
    data = "Hello Nexus World"
    if TextProcessor().validate(data):
        print("Validation: Text data verified")
    run_processor(TextProcessor(), data)

    print("Initializing Log Processor...")
    data = "ERROR: Connection timeout"
    if LogProcessor().validate(data):
        print("Validation: Log entry verified")
    run_processor(LogProcessor(), data)

    print("=== Polymorphic Processing Demo ===\n")
    polymorphic_demo()
    print()
    print("Foundation systems online. Nexus ready for advanced streams")


if __name__ == "__main__":
    main()
