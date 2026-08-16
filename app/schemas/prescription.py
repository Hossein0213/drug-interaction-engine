from pydantic import BaseModel, Field

from app.schemas.drug import Drug


class Prescription(BaseModel):
    prescription_id: str = Field(min_length = 1)
    patient_age: int | None = Field(default = None, ge = 0, le = 130)
    drugs: list[Drug] = Field(default_factory = list)