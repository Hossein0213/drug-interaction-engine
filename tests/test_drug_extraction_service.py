from app.schemas.drug import Drug
from app.schemas.prescription import Prescription
from app.services.drug_extraction_service import DrugExtractionService


def test_extract_drugs() -> None:
    prescription = Prescription(
        prescription_id="RX-001",
        patient_age=52,
        drugs=[
            Drug(
                name="Wrfarin",
                dosage="5 gm",
                frequency="Once daily",
            ),
            Drug(
                name="Asparin",
                dosage="81 gm",
                frequency="Once daily",
            )
        ],
    )

    service = DrugExtractionService()

    result = service.extract_drugs(prescription)


    assert len(result) == 2
    assert result[0].name == "Wrfarin"
    assert result[1].name == "Asparin"
