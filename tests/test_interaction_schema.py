import pytest
from pydantic import ValidationError

from app.schemas.interaction import Interaction, InteractionSeverity



def test_valid_interaction() -> None:
    interaction = Interaction(
        drug_a="Warfarin",
        drug_b="Aspirin",
        severity=InteractionSeverity.HIGH,
        description="Potentially significant interaction.",
        evidence="Medical database",
    )

    assert interaction.drug_a == "Warfarin"
    assert interaction.drug_b == "Aspirin"
    assert interaction.severity == InteractionSeverity.HIGH



def test_invalid_severity() -> None:
    with pytest.raises(ValidationError):
        Interaction(
            drug_a="Warfarin",
            drug_b="Aspirin",
            severity="banana",  # This will cause a validation error
            description="Invalid test.",
            evidence="Test",
        )

def test_missing_required_field() -> None:
    with pytest.raises(ValidationError):
        Interaction(
            drug_a="Warfarin",
            drug_b="Aspirin",
            severity=InteractionSeverity.HIGH,
            description="Missing evidence.",
        )