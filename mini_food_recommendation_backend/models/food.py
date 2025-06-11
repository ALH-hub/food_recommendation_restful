# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from .. import db

food_ingredient = db.Table(
    'food_ingredients',
    db.Column('food_id', db.Integer, db.ForeignKey('foods.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
)

class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.relationship('Ingredient', secondary=food_ingredient, back_populates='foods')

    #Relationships
    consumption = db.relationship('FoodConsumption', back_populates='food')
    images = db.relationship('FoodImage', back_populates='food')


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    foods = db.relationship('Food', secondary=food_ingredient, back_populates='ingredients')

    def __repr__(self):
        return f'<Ingredient {self.id} - {self.name}>'

    def __str__(self):
        return self.name