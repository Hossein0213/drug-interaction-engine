from app.schemas.drug import Drug
from app.schemas.prescription import Prescription


class DrugExtractionService:

    def extract_drugs(self, prescription: Prescription) -> list[Drug]:
        return prescription.drugs