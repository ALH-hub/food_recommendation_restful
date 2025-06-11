# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

# food recommendation service for a person based on their food consumption history
from ..models.food_consumption import FoodConsumption
from ..models.person import Person
from ..services.allergy_probability import AllergyProbabilityService
from ..models.food import Food

class FoodRecommendationService:
    @staticmethod
    def get_recommendations(person_id, limit=5):
        person = Person.query.get(person_id)
        if not person:
            raise ValueError("Person not found")

        consumptions = FoodConsumption.query.filter_by(user_id=person_id).all()
        if not consumptions:
            return []

        food_ids = [c.food_id for c in consumptions]
        food_items = Food.query.filter(Food.id.in_(food_ids)).all()

        recommendations = []
        for food in food_items:
            allergy_probability = AllergyProbabilityService.calculate_allergy_probability(person_id, food.id)
            recommendations.append({
                'food_id': food.id,
                'name': food.name,
                'allergy_probability': allergy_probability
            })

        recommendations.sort(key=lambda x: x['allergy_probability'])
        return recommendations[:limit]