# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from .. import db

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=True)

    # Relationships
    food_consumptions = db.relationship('FoodConsumption', back_populates='person')
    weekly_plans = db.relationship('WeeklyPlan', back_populates='person')

    def __repr__(self):
        return f'<Person {self.id} - {self.name}, Age: {self.age}>'