from pydantic import BaseModel, Field

class Drug(BaseModel):
    name: str = Field(min_length = 1)
    dosage: str | None = None
    frequency: str | None = None