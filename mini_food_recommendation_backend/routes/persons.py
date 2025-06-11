# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from flask import Blueprint, request, jsonify
from ..models import Person, Food
from ..config import db

persons_bp = Blueprint('persons', __name__)

@persons_bp.route('/persons', methods=['POST'])
def add_person():
    name = request.json.get('name')
    age = request.json.get('age', None)
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    person = Person(name=name, age=age)
    db.session.add(person)
    db.session.commit()
    return jsonify({'id': person.id, 'name': person.name, 'age': person.age}), 201

@persons_bp.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'age': p.age} for p in persons])

@persons_bp.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get_or_404(person_id)
    return jsonify({'id': person.id, 'name': person.name})

@persons_bp.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = Person.query.get_or_404(person_id)
    name = request.json.get('name', person.name)

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    person.name = name
    db.session.commit()
    return jsonify({'id': person.id, 'name': person.name})

@persons_bp.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'}), 204

@persons_bp.route('/persons/search', methods=['GET'])
def search_persons():
    query = request.args.get('query', '')
    persons = Person.query.filter(Person.name.ilike(f'%{query}%')).all()
    return jsonify([{'id': p.id, 'name': p.name} for p in persons])

@persons_bp.route('/persons/<int:person_id>/foods', methods=['GET'])
def get_person_foods(person_id):
    person = Person.query.get_or_404(person_id)
    foods = person.foods
    return jsonify([{'id': f.id, 'name': f.name} for f in foods])

@persons_bp.route('/persons/<int:person_id>/foods/<int:food_id>', methods=['POST'])
def add_food_to_person(person_id, food_id):
    person = Person.query.get_or_404(person_id)
    food = Food.query.get_or_404(food_id)

    if food in person.foods:
        return jsonify({'error': 'Food already added to this person'}), 400

    person.foods.append(food)
    db.session.commit()
    return jsonify({'message': 'Food added to person successfully'}), 201

@persons_bp.route('/persons/<int:person_id>/foods/<int:food_id>', methods=['DELETE'])
def remove_food_from_person(person_id, food_id):
    person = Person.query.get_or_404(person_id)
    food = Food.query.get_or_404(food_id)

    if food not in person.foods:
        return jsonify({'error': 'Food not found for this person'}), 404

    person.foods.remove(food)
    db.session.commit()
    return jsonify({'message': 'Food removed from person successfully'}), 204

@persons_bp.route('/persons/<int:person_id>/foods/<int:food_id>', methods=['PUT'])
def update_person_food(person_id, food_id):
    person = Person.query.get_or_404(person_id)
    food = Food.query.get_or_404(food_id)

    if food not in person.foods:
        return jsonify({'error': 'Food not found for this person'}), 404

    # Assuming we want to update the food details, which is not typical in this context
    # but for the sake of completeness, let's assume we can update the food name.
    new_food_name = request.json.get('name', food.name)

    if not new_food_name:
        return jsonify({'error': 'Food name is required'}), 400

    food.name = new_food_name
    db.session.commit()

    return jsonify({'id': food.id, 'name': food.name}), 200
