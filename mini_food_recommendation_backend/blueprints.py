# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from .routes.foods import foods_bp
from .routes.persons import persons_bp
from .routes.food_recommendation import rec_bp as food_recommendation_bp
from .routes.allergy_probability import rec_bp as allergy_probability_bp
from .routes.food_consumptions import food_consumptions_bp
from .routes.weekly_plan import weekly_plan_bp
from .routes.buffet_manage import buffet_bp

def register_blueprints(app):
    app.register_blueprint(foods_bp)
    app.register_blueprint(persons_bp)
    app.register_blueprint(food_recommendation_bp)
    app.register_blueprint(allergy_probability_bp)
    app.register_blueprint(food_consumptions_bp)
    app.register_blueprint(weekly_plan_bp)
    app.register_blueprint(buffet_bp)