# AUTHOR: ALHADJI OUMATE
# STUDENT ID: 22U2033

import random
import datetime
from mini_food_recommendation_backend.app import app
from mini_food_recommendation_backend.models import (
    Person, Food, Ingredient, FoodConsumption, FoodImage,
    WeeklyPlan, BuffetPlan, BuffetFood
)
from mini_food_recommendation_backend.config import db
from sqlalchemy import text

with app.app_context():
    # Clear existing data (optional)
    # Delete from association table first
    db.session.execute(text('DELETE FROM food_ingredients'))
    db.session.query(BuffetFood).delete()
    db.session.query(BuffetPlan).delete()
    db.session.query(WeeklyPlan).delete()
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
            image_data=bytes([random.randint(0, 255) for _ in range(100)]),
            content_type="image/png"
        )
        db.session.add(fi)
    db.session.commit()

    # 6. WeeklyPlans
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for person in persons:
        for day in days:
            # Each person gets 1-2 foods per day
            for food in random.sample(foods, random.randint(1, 2)):
                wp = WeeklyPlan(person_id=person.id, day_of_week=day, food_id=food.id)
                db.session.add(wp)
    db.session.commit()

    # 7. BuffetPlans and BuffetFoods
    for i in range(5):
        buffet = BuffetPlan(
            event_name=f"Event {i+1}",
            guest_count=random.randint(20, 100)
        )
        db.session.add(buffet)
        db.session.flush()  # Get buffet.id
        for food in random.sample(foods, random.randint(3, 6)):
            servings = buffet.guest_count  # 1 serving per guest
            bf = BuffetFood(buffet_id=buffet.id, food_id=food.id, servings=servings)
            db.session.add(bf)
    db.session.commit()

    print("Inserted sample records for all tables.")