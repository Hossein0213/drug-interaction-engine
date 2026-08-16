import pytest
from pydantic import ValidationError
from app.schemas.drug import Drug
from app.schemas.prescription import Prescription



def test_valid_drug() -> None:
    drug = Drug(
        name = "Warfarin",
        dosage = "5 mg",
        frequency = "once daily",
    )


    assert drug.name == "Warfarin"
    assert drug.dosage == "5 mg"



def test_invalid_drug_name() -> None:
    with pytest.raises(ValidationError):
        Drug(name = "")


def test_valid_prescription() -> None:
    prescription = Prescription(
        prescription_id = "RX-001",
        patient_age = 52,
        drugs=[
            Drug(
                name="Warfarin",
                dosage="5 mg",
                frequency="once daily",
            )
        ],
    )


    assert prescription.prescription_id == "RX-001"
    assert len(prescription.drugs) == 1




def test_invalid_patient_age() -> None:
    with pytest.raises(ValidationError):
        Prescription(
            prescription_id = "RX-001",
            patient_age = 150,
        )