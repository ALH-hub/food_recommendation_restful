# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from .. import db

class FoodImage(db.Model):
    __tablename__ = 'food_images'

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)
    content_type = db.Column(db.String(50), nullable=False)

    food = db.relationship('Food', back_populates='images')

    def __repr__(self):
        return f'<FoodImage {self.id} for Food {self.food_id}>'