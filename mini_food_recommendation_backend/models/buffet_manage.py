# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from ..config import db

class BuffetPlan(db.Model):
    __tablename__ = 'buffet_plans'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(128), nullable=False)
    guest_count = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

class BuffetFood(db.Model):
    __tablename__ = 'buffet_foods'
    id = db.Column(db.Integer, primary_key=True)
    buffet_id = db.Column(db.Integer, db.ForeignKey('buffet_plans.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)
    servings = db.Column(db.Integer, nullable=False)

    buffet = db.relationship('BuffetPlan', backref='foods')
    food = db.relationship('Food')