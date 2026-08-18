from app.schemas.drug import Drug
from app.schemas.prescription import Prescription
from app.services.prescription_service import PrescriptionService, prescription_service


def test_validate_prescription() -> None:
    service = PrescriptionService()


    prescription = Prescription(
        prescription_id="RX-001",
        patient_age=52,
        drugs=[
            Drug(
                name="Warfarin",
                dosage="5 mg",
                frequency="Once daily",
            )
        ],
    )


    result = service.validate_prescription(prescription)


    assert result == prescription
    assert result.prescription_id == "RX-001"
    assert len(result.drugs) == 1