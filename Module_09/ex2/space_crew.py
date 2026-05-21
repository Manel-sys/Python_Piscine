try:
    from pydantic import BaseModel, Field, ValidationError, model_validator  # type: ignore # noqa
    from pydantic_core import PydanticCustomError as Pe  # type: ignore
except ImportError:
    raise SystemExit("Error: Module pydantic is required. Install it,"
                     " in a virtual environment, using pip install pydantic")


from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True

    def show(self) -> None:
        print(f"- {self.name} ({self.rank.value}) - {self.specialization}")


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise Pe("mission_id_start", "Mission ID must start with 'M'")

        count: int = 0
        count_expert: int = 0
        for member in self.crew:
            if member.rank in (Rank.CAPTAIN, Rank.COMMANDER):
                count += 1
            if member.years_experience >= 5:
                count_expert += 1
        if count == 0:
            raise Pe("command_nbr", "Mission must have at least one Commander"
                     " or Captain")
        if self.duration_days > 365:
            if count_expert / len(self.crew) < 0.5:
                raise Pe("long_mission__experts", "Long missions (> 365 days) "
                         "need 50% experienced crew (5+ years)")
        if not all(member.is_active for member in self.crew):
            raise Pe("all_active_members", "All crew members must be active")

        return self

    def display(self) -> None:
        print("Valid mission created")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for member in self.crew:
            member.show()


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        member_1: CrewMember = CrewMember(
            member_id="001", name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=33, specialization="Mission Command",
            years_experience=5,
        )

        member_2: CrewMember = CrewMember(
            member_id="002", name="John Smith",
            rank=Rank.LIEUTENANT,
            age=28, specialization="Navigation",
            years_experience=4,
        )

        member_3: CrewMember = CrewMember(
            member_id="003", name="Alice Johnson",
            rank=Rank.OFFICER,
            age=45, specialization="Engineering",
            years_experience=7,
        )

        crew_1: list[CrewMember] = [member_1,
                                    member_2,
                                    member_3,
                                    ]

        valid_mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2030, 7, 12),
            duration_days=900,
            crew=crew_1,
            budget_millions=2500.0
        )

        valid_mission.display()
        print()

        print("=" * 40)
        crew_2: list[CrewMember] = [member_2,
                                    member_3
                                    ]

        invalid_mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2030, 7, 12),
            duration_days=900,
            crew=crew_2,
            budget_millions=2500.0
        )

        invalid_mission.display()
        print()

    except ValidationError as e:
        for error in e.errors():
            print("Expected validation error:")
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
