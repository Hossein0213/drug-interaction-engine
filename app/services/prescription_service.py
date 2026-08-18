from app.schemas.prescription import Prescription

class PrescriptionService:
    """Application service for prescription-related operations."""

    def validate_prescription(
            self,
            prescription: Prescription,
    ) -> Prescription:
        return prescription


prescription_service = PrescriptionService()