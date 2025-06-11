# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from ..models.food_consumption import FoodConsumption

class AllergyProbabilityService:
    @staticmethod
    def calculate_allergy_probability(person_id, food_id):
        consumptions = FoodConsumption.query.filter_by(user_id=person_id).all()

        if not consumptions:
            return 0.0

        total_consumptions = len(consumptions)
        food_consumptions = sum(1 for c in consumptions if c.food_id == food_id)

        if total_consumptions == 0:
            return 0.0

        probability = food_consumptions / total_consumptions

        return probability