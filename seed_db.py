# Place this script in your project root or run in flask shell
import random
import datetime
from mini_food_recommendation_backend.app import app
from mini_food_recommendation_backend.models import Person, Food, Ingredient, FoodConsumption, FoodImage
from mini_food_recommendation_backend.config import db

with app.app_context():
    # Clear existing data (optional)
    db.session.query(FoodConsumption).delete()
    db.session.query(FoodImage).delete()
    db.session.query(Person).delete()
    db.session.query(Food).delete()
    db.session.query(Ingredient).delete()
    db.session.commit()

    # 1. Persons
    persons = []
    for i in range(1, 51):
        p = Person(name=f"Person {i}", age=random.randint(18, 60))
        db.session.add(p)
        persons.append(p)
    db.session.commit()

    # 2. Ingredients
    ingredients = []
    for i in range(1, 51):
        ing = Ingredient(name=f"Ingredient {i}")
        db.session.add(ing)
        ingredients.append(ing)
    db.session.commit()

    # 3. Foods
    foods = []
    for i in range(1, 51):
        f = Food(name=f"Food {i}")
        # Add 2-5 random ingredients to each food
        f.ingredients = random.sample(ingredients, random.randint(2, 5))
        db.session.add(f)
        foods.append(f)
    db.session.commit()

    # 4. FoodConsumptions
    for i in range(50):
        fc = FoodConsumption(
            timestamp=datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)),
            food_id=random.choice(foods).id,
            user_id=random.choice(persons).id
        )
        db.session.add(fc)
    db.session.commit()

    # 5. FoodImages
    for i in range(50):
        fi = FoodImage(
            food_id=random.choice(foods).id,
            image_data=bytes([random.randint(0, 255) for _ in range(100)]),  # Dummy binary data
            content_type="image/png"
        )
        db.session.add(fi)
    db.session.commit()

    print("Inserted 50 records for each table.")