try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    raise SystemExit("Error: Module pydantic is required. Install it,"
                     " in a virtual environment, using pip install pydantic")


from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    try:
        print("=" * 40)
        station_1: SpaceStation = SpaceStation(station_id="ISS001",
                                               name="International"
                                               " Space Station",
                                               crew_size=6,
                                               power_level=85.5,
                                               oxygen_level=92.3,
                                               last_maintenance=datetime(2025,
                                                                         7,
                                                                         12),
                                               notes="All systems working!")

        print("Valid station created:")
        print(f"ID: {station_1.station_id}")
        print(f"Name: {station_1.name}")
        print(f"Crew: {station_1.crew_size} people")
        print(f"Power: {station_1.power_level}%")
        print(f"Oxygen: {station_1.oxygen_level}%")
        if station_1.is_operational:
            print("Status: Operational")
        else:
            print("Status: Not Operational")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])

    try:
        print("=" * 40)
        station_2: SpaceStation = SpaceStation(station_id="ISS002",
                                               name="Hypothetical Space"
                                               " Station",
                                               crew_size=30,
                                               power_level=75.0,
                                               oxygen_level=50.5,
                                               last_maintenance=datetime(2025,
                                                                         7,
                                                                         12),
                                               notes="Checking...")
        print("Valid station created:")
        print(f"ID: {station_2.station_id}")
        print(f"Name: {station_2.name}")
        print(f"Crew: {station_2.crew_size} people")
        print(f"Power: {station_2.power_level}%")
        print(f"Oxygen: {station_2.oxygen_level}%")
        if station_2.is_operational:
            print("Status: Operational")
        else:
            print("Status: Not Operational")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
