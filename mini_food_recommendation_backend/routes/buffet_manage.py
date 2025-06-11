# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from flask import Blueprint, request, jsonify
from ..models.food import Food
from ..models.buffet_manage import BuffetPlan, BuffetFood
from ..config import db

buffet_bp = Blueprint('buffet', __name__)

@buffet_bp.route('/buffet', methods=['POST'])
def create_buffet():
    data = request.json
    event_name = data.get('event_name')
    guest_count = data.get('guest_count')
    food_ids = data.get('food_ids', [])

    if not event_name or not guest_count or not food_ids:
        return jsonify({"error": "event_name, guest_count, and food_ids are required"}), 400

    buffet = BuffetPlan(event_name=event_name, guest_count=guest_count)
    db.session.add(buffet)
    db.session.flush()

    for food_id in food_ids:
        food = Food.query.get(food_id)
        if food:
            servings = guest_count  # Simple logic: 1 serving per guest
            buffet_food = BuffetFood(buffet_id=buffet.id, food_id=food_id, servings=servings)
            db.session.add(buffet_food)
    db.session.commit()
    return jsonify({"message": "Buffet plan created", "buffet_id": buffet.id}), 201

@buffet_bp.route('/buffet/<int:buffet_id>', methods=['GET'])
def get_buffet(buffet_id):
    buffet = BuffetPlan.query.get_or_404(buffet_id)
    foods = [
        {
            "food_id": bf.food.id,
            "food_name": bf.food.name,
            "servings": bf.servings
        }
        for bf in buffet.foods
    ]
    return jsonify({
        "event_name": buffet.event_name,
        "guest_count": buffet.guest_count,
        "foods": foods
    })

@buffet_bp.route('/buffet/<int:buffet_id>', methods=['DELETE'])
def delete_buffet(buffet_id):
    buffet = BuffetPlan.query.get_or_404(buffet_id)
    db.session.delete(buffet)
    db.session.commit()
    return jsonify({"message": "Buffet plan deleted successfully"})

@buffet_bp.route('/buffet', methods=['GET'])
def list_buffets():
    buffets = BuffetPlan.query.all()
    result = []
    for buffet in buffets:
        foods = [
            {
                "food_id": bf.food.id,
                "food_name": bf.food.name,
                "servings": bf.servings
            }
            for bf in buffet.foods
        ]
        result.append({
            "buffet_id": buffet.id,
            "event_name": buffet.event_name,
            "guest_count": buffet.guest_count,
            "foods": foods
        })
    return jsonify(result)