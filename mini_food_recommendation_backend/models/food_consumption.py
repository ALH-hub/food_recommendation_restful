# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from .. import db

class FoodConsumption(db.Model):
    __tablename__ = 'food_consumptions'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('persons.id'), nullable=False)
    person = db.relationship('Person', back_populates='food_consumptions')

    #user = db.relationship('User', back_populates='food_consumptions')
    food = db.relationship('Food', back_populates='consumption')

    def __repr__(self):
        return f'<FoodConsumption {self.id} - User {self.user_id} consumed Food {self.food_id}>'