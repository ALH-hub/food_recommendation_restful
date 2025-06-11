# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from ..config import db

class WeeklyPlan(db.Model):
    __tablename__ = 'weekly_plans'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'), nullable=False)
    day_of_week = db.Column(db.String(16), nullable=False)  # e.g., "Monday"
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)

    person = db.relationship('Person', back_populates='weekly_plans')
    food = db.relationship('Food')