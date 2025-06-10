from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False