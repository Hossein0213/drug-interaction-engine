from app.schemas.drug import Drug


class InteractionService:

    def generate_pairs(self, drugs: list[Drug]) -> list[tuple[Drug, Drug]]:
        pairs: list[tuple[Drug, Drug]] = []

        for i in range(len(drugs)):
            for j in range(i +1, len(drugs)):
                pairs.append((drugs[i], drugs[j]))

        return pairs