from enum import Enum
from pydantic import BaseModel


class InteractionSeverity(str, Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    CONTRAINDICATED = "Contraindicated"

class Interaction(BaseModel):
    drug_a: str
    drug_b: str
    severity: InteractionSeverity
    description: str
    evidence: str