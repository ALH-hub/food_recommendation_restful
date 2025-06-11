# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from flask import Blueprint, request, jsonify
from ..services.allergy_probability import AllergyProbabilityService


rec_bp = Blueprint('allergy_probability', __name__)

@rec_bp.route('/allergy_probability/<int:person_id>/<int:food_id>', methods=['GET'])
def get_allergy_probability(person_id, food_id):
    try:
        probability = AllergyProbabilityService.calculate_allergy_probability(person_id, food_id)
        return jsonify({'probability': probability}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500