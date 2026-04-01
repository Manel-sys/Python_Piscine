from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.id: str = stream_id
        self.proc_count: int = 0

    def _to_list(self, data: Any) -> List[Any]:
        if isinstance(data, List):
            return data
        raise TypeError(f"Expected a list as input, got "
                        f"{data.__class__.__name__}")

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        try:
            data_batch = self._to_list(data_batch)
        except TypeError as e:
            print(f"filter_data error: {e}")
            return []

        if criteria is None:
            return data_batch

        return [x for x in data_batch if criteria in x]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"processes": self.proc_count}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type: str = "Environmental Data"
        self.avg_temp: float = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        try:
            data_batch = self._to_list(data_batch)
        except TypeError as e:
            print(f"filter_data error: {e}")
            return []

        if criteria is None:
            return data_batch

        filtered: List[Any] = []

        for p in data_batch:
            try:
                proc: List[str] = p.split(":")
                if len(proc) != 2:
                    raise ValueError(f"Expected format for list "
                                     f"arg '<param1>:<param2>' got '{p}'")
                if criteria == "high":
                    if proc[0].strip() == "temp" and float(proc[1]) > 38:
                        filtered.append(p)
                elif criteria == "low":
                    if proc[0].strip() == "temp" and float(proc[1]) <= 0:
                        filtered.append(p.strip())

            except AttributeError:
                print(f"Error while filtering {p} - expected a str got "
                      f"{p.__class__.__name__}")

            except ValueError as e:
                print(f"Error while filtering {p} - {e}")

        return filtered

    def process_batch(self, data_batch: List[Any]) -> str:

        valid_prefix: List[str] = ["temp", "humidity", "pressure"]

        try:
            data_batch = self._to_list(data_batch)
        except TypeError as e:
            print(f"process_batch error: {e}")
            return ""

        temps: List[float] = []

        for p in data_batch:
            try:
                proc: List[str] = p.split(":")
                if len(proc) != 2:
                    raise ValueError("Expected format for list "
                                     "arg '<param1>:<param2>'")

                if proc[0].strip() not in valid_prefix:
                    raise ValueError(f"Valid values for <param1> of "
                                     f"arg <param1>:<param2>"
                                     f" are {valid_prefix}")
                self.proc_count += 1
                if proc[0].strip() == "temp":
                    temps.append(float(proc[1]))

            except AttributeError:
                print(f"Error while filtering {p} - expected a str got "
                      f"{p.__class__.__name__}")

            except ValueError as e:
                print(f"Error while processing '{p}' - {e}")

        temp_count: int = len(temps)
        total_sum: float = sum(temps)
        try:
            self.avg_temp = total_sum / temp_count
        except ZeroDivisionError:
            print("Tried to divide by zero")

        return (f"{self.proc_count} readings processed,"
                f" avg temp: {self.avg_temp}°C")

    def get_stats(self):
        return {"id": self.id, "type": self.type,
                "proc_count": self.proc_count,
                "avg_temp": self.avg_temp
                }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type: str = "Financial Data"
        self.net_flow: float = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        try:
            data_batch = self._to_list(data_batch)
        except TypeError as e:
            print(f"filter_data error: {e}")
            return []

        if criteria is None:
            return data_batch

        filtered: List[Any] = []

        for p in data_batch:
            try:
                proc: List[str] = p.split(":")
                if len(proc) != 2:
                    raise ValueError("Expected format for list "
                                     "arg '<param1>:<param2>'")

                if not (proc[0].strip() == "buy" or proc[0].strip() == "sell"):
                    raise ValueError("Expected <param1> of arg <param1>"
                                     ":<param2> to be <sell> or <buy>")

                if criteria == "high":
                    if float(proc[1]) > 100:
                        filtered.append(p.strip())

            except AttributeError:
                print(f"Error while filtering {p} - expected a str got "
                      f"{p.__class__.__name__}")

            except ValueError as e:
                print(f"Error while filtering {p} - {e}")
        return filtered

    def process_batch(self, data_batch: List[Any]) -> str:

        try:
            data_batch = self._to_list(data_batch)
        except TypeError as e:
            print(f"process_batch error: {e}")
            return ""

        transactions: List[float] = []

        for p in data_batch:
            try:
                proc: List[str] = p.split(":")
                if len(proc) != 2:
                    raise ValueError("Expected format for list "
                                     "arg '<param1>:<param2>'")

                if not (proc[0].strip() == "buy" or proc[0].strip() == "sell"):
                    raise ValueError("Expected <param1> of arg <param1>"
                                     ":<param2> to be <sell> or <buy>")

                if proc[0].strip() == "buy":
                    transactions.append(float(proc[1]))
                elif proc[0].strip() == "sell":
                    transactions.append(-float(proc[1]))

                self.proc_count += 1
                self.net_flow = sum(transactions)
                if self.net_flow.is_integer():
                    self.net_flow = int(self.net_flow)

            except AttributeError:
                print(f"Error while processing {p} - expected a str got "
                      f"{p.__class__.__name__}")

            except ValueError as e:
                print(f"Error while processing {p} - {e}")

        return f"{self.proc_count} operations, net flow: {self.net_flow:+}"

    def get_stats(self):
        return {"id": self.id, "type": self.type,
                "proc_count": self.proc_count,
                "net_flow": self.net_flow
                }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type: str = "System Events"
        self.error_count: int = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        try:
            data_batch = self._to_list(data_batch)
        except TypeError as e:
            print(f"filter_data error: {e}")
            return []

        if criteria is None:
            return data_batch

        filtered: List[Any] = []

        for p in data_batch:
            try:
                if not isinstance(p, str):
                    raise TypeError()

                if criteria == "high":
                    if p.strip() == "error":
                        filtered.append(p)
            except TypeError:
                print(f"Error while filtering {p} - expected a str got "
                      f"{p.__class__.__name__}")

        return filtered

    def process_batch(self, data_batch: List[Any]) -> str:

        valid_event: List[str] = ["login", "error", "logout"]

        try:
            data_batch = self._to_list(data_batch)
        except TypeError as e:
            print(f"process_batch error: {e}")
            return ""

        for p in data_batch:
            try:
                if not isinstance(p, str):
                    raise TypeError()

                if p.strip() not in valid_event:
                    raise ValueError()

                self.proc_count += 1
                if p.strip() == "error":
                    self.error_count += 1

            except TypeError:
                print(f"Error while processing {p} - expected a str got "
                      f"{p.__class__.__name__}")
            except ValueError:
                print(f"Error while processing {p} - not a valid event")

        return f"{self.proc_count} events, {self.error_count} error detected"

    def get_stats(self):
        return {"id": self.id, "type": self.type,
                "proc_count": self.proc_count,
                "error_count": self.error_count
                }


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:

        if isinstance(stream, DataStream):
            self.streams.append(stream)
        else:
            print(f"Expected a DataStream object, got "
                  f"{stream.__class__.__name__}")

    def run_processor(self, batches: List[List[Any]]) -> None:
        print("Processing mixed stream types through unified interface...\n")

        for i, batch in enumerate(batches, 1):
            print(f"Batch {i} Results:")
            




def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_001 = SensorStream("SENSOR_001")
    data_stream: str = "temp:22.5, humidity:65, pressure:1013"
    data_batch: List[Any] = data_stream.split(",")

    print(f"Stream ID: {sensor_001.get_stats()['id']}, "
          f"Type: {sensor_001.get_stats()['type']}")
    print(f"Processing sensor batch: [{data_stream}]")

    result: str = sensor_001.process_batch(["temp:to", "temp:100"])
    if result:
        print(f"Sensor analysis: {result}")

    print("\nInitializing Transaction Stream...")
    trans_001 = TransactionStream("TRANS_001")
    data_stream = "buy:100, sell:150, buy:75"
    data_batch = data_stream.split(",")

    print(f"Stream ID: {trans_001.get_stats()['id']}, "
          f"Type: {trans_001.get_stats()['type']}")
    print(f"Processing transaction batch: [{data_stream}]")

    result = trans_001.process_batch(data_batch)
    if result:
        print(f"Transaction analysis: {result}")

    print("\nInitializing Event Stream...")
    event_001 = EventStream("EVENT_001")
    data_stream = "login, error, logout"
    data_batch = data_stream.split(",")

    print(f"Stream ID: {event_001.get_stats()['id']}, "
          f"Type: {event_001.get_stats()['type']}")
    print(f"Processing event batch: [{data_stream}]")

    result = event_001.process_batch(data_batch)
    if result:
        print(f"Event analysis: {result}")


if __name__ == "__main__":
    main()
