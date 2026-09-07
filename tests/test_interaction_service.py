from app.schemas.drug import Drug
from app.services.interaction_service import InteractionService


def test_generate_unique_drug_pairs():

    drugs = [
        Drug(name="Drug A", dosage="10 mg", frequency="once daily"),
        Drug(name="Drug B", dosage="20 mg", frequency="twice daily"),
        Drug(name="Drug C", dosage="5 mg", frequency="once daily"),
        Drug(name="Drug D", dosage="50 mg", frequency="once daily"),
    ]

    service = InteractionService()

    pairs = service.generate_pairs(drugs)

    assert len(pairs) == 6  # There should be 6 unique pairs for 4 drugs

    assert pairs[0] == (drugs[0], drugs[1])
    assert pairs[1] == (drugs[0], drugs[2])
    assert pairs[2] == (drugs[0], drugs[3])
    assert pairs[3] == (drugs[1], drugs[2])
    assert pairs[4] == (drugs[1], drugs[3])
    assert pairs[5] == (drugs[2], drugs[3])