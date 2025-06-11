# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from flask import Blueprint, request, jsonify
from ..models.food import Food, Ingredient
from ..config import db

foods_bp = Blueprint('foods', __name__)

@foods_bp.route('/foods', methods=['POST'])
def add_food():
    name = request.json.get('name')
    ingredient_names = request.json.get('ingredients', [])
    food = Food(name=name)
    db.session.add(food)
    db.session.commit()  # Commit first to get food.id

    for ing_name in ingredient_names:
        ingredient = Ingredient.query.filter_by(name=ing_name).first()
        if not ingredient:
            ingredient = Ingredient(name=ing_name)
            db.session.add(ingredient)
            db.session.commit()
        food.ingredients.append(ingredient)
    db.session.commit()
    return jsonify({'id': food.id, 'name': food.name}), 201

@foods_bp.route('/foods', methods=['GET'])
def get_foods():
    foods = Food.query.all()
    return jsonify([
        {'id': f.id, 'name': f.name, 'ingredients': [i.name for i in f.ingredients]}
        for f in foods
    ])

@foods_bp.route('/foods/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = Food.query.get_or_404(food_id)
    return jsonify({
        'id': food.id,
        'name': food.name,
        'ingredients': [i.name for i in food.ingredients]
    })

@foods_bp.route('/foods/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    food = Food.query.get_or_404(food_id)
    name = request.json.get('name', food.name)
    ingredient_names = request.json.get('ingredients', [])

    food.name = name
    food.ingredients.clear()
    for ing_name in ingredient_names:
        ingredient = Ingredient.query.filter_by(name=ing_name).first()
        if not ingredient:
            ingredient = Ingredient(name=ing_name)
            db.session.add(ingredient)
            db.session.commit()
        food.ingredients.append(ingredient)
    db.session.commit()
    return jsonify({'id': food.id, 'name': food.name})

@foods_bp.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return jsonify({'message': 'Food deleted successfully'}), 204

@foods_bp.route('/ingredients', methods=['POST'])
def add_ingredient():
    name = request.json.get('name')
    ingredient = Ingredient(name=name)
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({'id': ingredient.id, 'name': ingredient.name}), 201

@foods_bp.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify([{'id': i.id, 'name': i.name} for i in ingredients])

@foods_bp.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    return jsonify({'id': ingredient.id, 'name': ingredient.name})

@foods_bp.route('/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    name = request.json.get('name', ingredient.name)
    ingredient.name = name
    db.session.commit()
    return jsonify({'id': ingredient.id, 'name': ingredient.name})

@foods_bp.route('/ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    db.session.delete(ingredient)
    db.session.commit()
    return jsonify({'message': 'Ingredient deleted successfully'}), 204

@foods_bp.route('/foods/search', methods=['GET'])
def search_foods():
    query = request.args.get('query', '')
    foods = Food.query.filter(Food.name.ilike(f'%{query}%')).all()
    return jsonify([
        {'id': f.id, 'name': f.name, 'ingredients': [i.name for i in f.ingredients]}
        for f in foods
    ])

@foods_bp.route('/ingredients/search', methods=['GET'])
def search_ingredients():
    query = request.args.get('query', '')
    ingredients = Ingredient.query.filter(Ingredient.name.ilike(f'%{query}%')).all()
    return jsonify([{'id': i.id, 'name': i.name} for i in ingredients])

@foods_bp.route('/foods/<int:food_id>/ingredients', methods=['GET'])
def get_food_ingredients(food_id):
    food = Food.query.get_or_404(food_id)
    return jsonify({
        'id': food.id,
        'name': food.name,
        'ingredients': [i.name for i in food.ingredients]
    })

@foods_bp.route('/ingredients/<int:ingredient_id>/foods', methods=['GET'])
def get_ingredient_foods(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    return jsonify({
        'id': ingredient.id,
        'name': ingredient.name,
        'foods': [f.name for f in ingredient.foods]
    })

@foods_bp.route('/foods/<int:food_id>/ingredients', methods=['POST'])
def add_ingredient_to_food(food_id):
    food = Food.query.get_or_404(food_id)
    ingredient_name = request.json.get('name')
    ingredient = Ingredient.query.filter_by(name=ingredient_name).first()

    if not ingredient:
        ingredient = Ingredient(name=ingredient_name)
        db.session.add(ingredient)
        db.session.commit()

    food.ingredients.append(ingredient)
    db.session.commit()

    return jsonify({'id': food.id, 'name': food.name, 'ingredients': [i.name for i in food.ingredients]}), 201

@foods_bp.route('/foods/<int:food_id>/ingredients/<int:ingredient_id>', methods=['DELETE'])
def remove_ingredient_from_food(food_id, ingredient_id):
    food = Food.query.get_or_404(food_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    if ingredient in food.ingredients:
        food.ingredients.remove(ingredient)
        db.session.commit()
        return jsonify({'message': 'Ingredient removed from food successfully'}), 204
    else:
        return jsonify({'message': 'Ingredient not found in food'}), 404

@foods_bp.route('/foods/<int:food_id>/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_food_ingredient(food_id, ingredient_id):
    food = Food.query.get_or_404(food_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    new_name = request.json.get('name', ingredient.name)
    ingredient.name = new_name

    db.session.commit()

    return jsonify({'id': food.id, 'name': food.name, 'ingredients': [i.name for i in food.ingredients]})

@foods_bp.route('/foods/<int:food_id>/ingredients/<int:ingredient_id>', methods=['GET'])
def get_food_ingredient(food_id, ingredient_id):
    food = Food.query.get_or_404(food_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    if ingredient in food.ingredients:
        return jsonify({'id': ingredient.id, 'name': ingredient.name})
    else:
        return jsonify({'message': 'Ingredient not found in food'}), 404

@foods_bp.route('/foods/<int:food_id>/ingredients/<int:ingredient_id>/exists', methods=['GET'])
def check_ingredient_in_food(food_id, ingredient_id):
    food = Food.query.get_or_404(food_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    exists = ingredient in food.ingredients
    return jsonify({'exists': exists})

@foods_bp.route('/foods/<int:food_id>/ingredients/<int:ingredient_id>/count', methods=['GET'])
def count_ingredient_in_food(food_id, ingredient_id):
    food = Food.query.get_or_404(food_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    count = food.ingredients.count(ingredient)
    return jsonify({'count': count})


@foods_bp.route('/foods/<int:food_id>/ingredients/<int:ingredient_id>/update', methods=['PUT'])
def update_food_ingredient_details(food_id, ingredient_id):
    food = Food.query.get_or_404(food_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    new_name = request.json.get('name', ingredient.name)
    ingredient.name = new_name

    db.session.commit()

    return jsonify({'id': food.id, 'name': food.name, 'ingredients': [i.name for i in food.ingredients]})

@foods_bp.route('/foods/<int:food_id>/ingredients/<int:ingredient_id>/delete', methods=['DELETE'])
def delete_food_ingredient(food_id, ingredient_id):
    food = Food.query.get_or_404(food_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    if ingredient in food.ingredients:
        food.ingredients.remove(ingredient)
        db.session.commit()
        return jsonify({'message': 'Ingredient removed from food successfully'}), 204
    else:
        return jsonify({'message': 'Ingredient not found in food'}), 404
