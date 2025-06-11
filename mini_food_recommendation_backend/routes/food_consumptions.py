# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from flask import Blueprint, request, jsonify
from ..models import FoodConsumption, Person, Food
from ..config import db
from datetime import datetime

food_consumptions_bp = Blueprint('food_consumptions', __name__)

@food_consumptions_bp.route('/consumptions', methods=['POST'])
def add_food_consumption():
  user_id = request.json.get('person_id')
  food_id = request.json.get('food_id')

  if not user_id or not food_id:
    return jsonify({'error': 'User ID and Food ID are required'}), 400

  person = Person.query.get(user_id)
  food = Food.query.get(food_id)

  if not person or not food:
    return jsonify({'error': 'Person or Food not found'}), 404

  consumption = FoodConsumption(
    user_id=user_id,
    food_id=food_id,
    timestamp=datetime.utcnow(),
    person=person,
    food=food
  )
  db.session.add(consumption)
  db.session.commit()

  return jsonify({
    'id': consumption.id,
    'user_id': consumption.user_id,
    'food_id': consumption.food_id,
    'timestamp': consumption.timestamp.isoformat()
  }), 201

@food_consumptions_bp.route('/consumptions', methods=['GET'])
def get_food_consumptions():
    consumptions = FoodConsumption.query.all()
    return jsonify([{
        'id': c.id,
        'user_id': c.user_id,
        'food_id': c.food_id,
        'timestamp': c.timestamp.isoformat()
    } for c in consumptions]), 200

@food_consumptions_bp.route('/consumptions/<int:consumption_id>', methods=['GET'])
def get_food_consumption(consumption_id):
    consumption = FoodConsumption.query.get_or_404(consumption_id)
    return jsonify({
        'id': consumption.id,
        'user_id': consumption.user_id,
        'food_id': consumption.food_id,
        'timestamp': consumption.timestamp.isoformat()
    }), 200

@food_consumptions_bp.route('/consumptions/<int:consumption_id>', methods=['DELETE'])
def delete_food_consumption(consumption_id):
    consumption = FoodConsumption.query.get_or_404(consumption_id)
    db.session.delete(consumption)
    db.session.commit()
    return jsonify({'message': 'Food consumption deleted successfully'}), 204

@food_consumptions_bp.route('/consumptions/person/<int:person_id>', methods=['GET'])
def get_person_food_consumptions(person_id):
    person = Person.query.get_or_404(person_id)
    consumptions = person.food_consumptions
    return jsonify([{
        'id': c.id,
        'user_id': c.user_id,
        'food_id': c.food_id,
        'timestamp': c.timestamp.isoformat()
    } for c in consumptions]), 200

@food_consumptions_bp.route('/consumptions/food/<int:food_id>', methods=['GET'])
def get_food_consumptions_by_food(food_id):
    food = Food.query.get_or_404(food_id)
    consumptions = food.consumption
    return jsonify([{
        'id': c.id,
        'user_id': c.user_id,
        'food_id': c.food_id,
        'timestamp': c.timestamp.isoformat()
    } for c in consumptions]), 200

@food_consumptions_bp.route('/consumptions/person/<int:person_id>/food/<int:food_id>', methods=['GET'])
def get_person_food_consumption(person_id, food_id):
    person = Person.query.get_or_404(person_id)
    food = Food.query.get_or_404(food_id)
    consumption = FoodConsumption.query.filter_by(user_id=person.id, food_id=food.id).first()

    if not consumption:
        return jsonify({'error': 'No consumption found for this person and food'}), 404

    return jsonify({
        'id': consumption.id,
        'user_id': consumption.user_id,
        'food_id': consumption.food_id,
        'timestamp': consumption.timestamp.isoformat()
    }), 200

@food_consumptions_bp.route('/consumptions/person/<int:person_id>/food/<int:food_id>', methods=['POST'])
def add_person_food_consumption(person_id, food_id):
    person = Person.query.get_or_404(person_id)
    food = Food.query.get_or_404(food_id)

    consumption = FoodConsumption(
        user_id=person.id,
        food_id=food.id,
        timestamp=datetime.utcnow(),
        person=person,
        food=food
    )
    db.session.add(consumption)
    db.session.commit()

    return jsonify({
        'id': consumption.id,
        'user_id': consumption.user_id,
        'food_id': consumption.food_id,
        'timestamp': consumption.timestamp.isoformat()
    }), 201

@food_consumptions_bp.route('/consumptions/person/<int:person_id>/food/<int:food_id>', methods=['DELETE'])
def delete_person_food_consumption(person_id, food_id):
    person = Person.query.get_or_404(person_id)
    food = Food.query.get_or_404(food_id)
    consumption = FoodConsumption.query.filter_by(user_id=person.id, food_id=food.id).first()

    if not consumption:
        return jsonify({'error': 'No consumption found for this person and food'}), 404

    db.session.delete(consumption)
    db.session.commit()
    return jsonify({'message': 'Food consumption deleted successfully'}), 204

@food_consumptions_bp.route('/consumptions/person/<int:person_id>/foods', methods=['GET'])
def get_person_foods(person_id):
    person = Person.query.get_or_404(person_id)
    foods = person.foods
    return jsonify([{'id': f.id, 'name': f.name} for f in foods]), 200
