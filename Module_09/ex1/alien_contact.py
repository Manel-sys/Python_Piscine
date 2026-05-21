try:
    from pydantic import BaseModel, Field, ValidationError, model_validator  # type: ignore # noqa
    from pydantic_core import PydanticCustomError as Pe  # type: ignore
except ImportError:
    raise SystemExit("Error: Module pydantic is required. Install it,"
                     " in a virtual environment, using pip install pydantic")


from enum import Enum
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise Pe("ac_prefix", "Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise Pe("physical_verified", "Physical contact reports"
                     " must be verified")
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise Pe("telepathic_witnesses", "Telepathic contact"
                     " requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise Pe("strong_signal_message", "Strong signals ( > 7.0)"
                     " should include received messages")

        return self

    def display(self) -> None:
        print("Valid contact report:")
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: '{self.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    try:
        print("=" * 40)
        contact_1: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1),
            location="Area 52, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli")

        contact_1.display()
        print()
    except ValidationError as e:
        for error in e.errors():
            print("Expected validation error:")
            print(f"{error['msg']}")

    try:
        print("=" * 40)
        contact_2: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1),
            location="Area 52, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli")

        contact_2.display()
        print()
    except ValidationError as e:
        for error in e.errors():
            print("Expected validation error:")
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
