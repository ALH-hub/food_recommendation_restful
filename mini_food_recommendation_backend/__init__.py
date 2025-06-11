# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from flask import Flask, jsonify
from flask_migrate import Migrate
from .config import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('mini_food_recommendation_backend.config.Config')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return jsonify({'message': "Welcome to the Mini Food Recommendation Backend!"})


    with app.app_context():
        #db.create_all()
        from .blueprints import register_blueprints
        register_blueprints(app)

    return app