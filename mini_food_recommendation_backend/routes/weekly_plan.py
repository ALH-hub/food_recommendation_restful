# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from flask import Blueprint, request, jsonify
from ..models.person import Person
from ..models.food import Food
from ..models.weekly_plan import WeeklyPlan
from ..config import db

weekly_plan_bp = Blueprint('weekly_plan', __name__)

@weekly_plan_bp.route('/weekly_plan/<int:person_id>', methods=['POST'])
def set_weekly_plan(person_id):
    person = Person.query.get_or_404(person_id)
    plan = request.json.get('plan', {})

    # Remove existing plans for this person
    WeeklyPlan.query.filter_by(person_id=person_id).delete()

    for day, food_ids in plan.items():
        for food_id in food_ids:
            food = Food.query.get(food_id)
            if food:
                wp = WeeklyPlan(person_id=person_id, day_of_week=day, food_id=food_id)
                db.session.add(wp)
    db.session.commit()
    return jsonify({"message": "Weekly plan set successfully"}), 201

@weekly_plan_bp.route('/weekly_plan/<int:person_id>', methods=['GET'])
def get_weekly_plan(person_id):
    person = Person.query.get_or_404(person_id)
    plans = WeeklyPlan.query.filter_by(person_id=person_id).all()
    result = {}
    for plan in plans:
        day = plan.day_of_week
        food = Food.query.get(plan.food_id)
        if day not in result:
            result[day] = []
        result[day].append({"food_id": food.id, "food_name": food.name})
    return jsonify({"person_id": person_id, "plan": result})

@weekly_plan_bp.route('/weekly_plan/<int:person_id>', methods=['DELETE'])
def delete_weekly_plan(person_id):
    person = Person.query.get_or_404(person_id)
    WeeklyPlan.query.filter_by(person_id=person_id).delete()
    db.session.commit()
    return jsonify({"message": "Weekly plan deleted successfully"})