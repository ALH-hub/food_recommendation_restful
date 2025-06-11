# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from ..services.food_recommendation import FoodRecommendationService
from flask import Blueprint, request, jsonify
from ..models.person import Person


rec_bp = Blueprint('food_recommendation', __name__)

@rec_bp.route('/recommendations/<int:person_id>', methods=['GET'])
def get_recommendations(person_id):
    try:
        person = Person.query.get(person_id)
        if not person:
            return jsonify({'error': 'Person not found'}), 404

        recommendations = FoodRecommendationService.get_recommendations(person_id)

        return jsonify(recommendations), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500