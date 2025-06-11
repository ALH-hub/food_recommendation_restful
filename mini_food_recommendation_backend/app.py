# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

from .config import db
from . import create_app


app = create_app()

if __name__ == '__main__':
    from .config import db
    with app.app_context():
        db.create_all()
    app.run(debug=True)