# Mini Food Recommendation Backend

## Table of Contents

- [Local Setup (Without Docker)](#local-setup-without-docker)
- [Available Routes](#available-routes)
  - [General](#general)
  - [Persons](#persons)
  - [Foods](#foods)
  - [Ingredients](#ingredients)
  - [Food Consumption](#food-consumption)
  - [Food Images](#food-images)
  - [Food Recommendation Routes](#food-recommendation-routes)
  - [Allergy Probability Routes](#allergy-probability-routes)
  - [Weekly Plan Routes](#weekly-plan-routes)
  - [Local Setup (Without Docker)](#local-setup-without-docker)
  - [Buffet Management Routes](#buffet-management-routes)
- [Database Model](#database-model)
- [Notes](#notes)
- [Author Information](#author-information)
- [License](#license)

  ***

  ## Local Setup (Without Docker)

  To run this project locally without Docker, follow these steps:

  1. **Clone the repository:**

  ```bash
  git clone <repository-url>
  cd mini_food_recommendation_backend
  ```

  2. **Create and activate a virtual environment:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

  3. **Install dependencies:**

  ```bash
  pip install -r requirements.txt
  ```

  4. **Set up environment variables:**

  - Create a `.env` file in the project root with your configuration (e.g., database URL).

  5. **Set up the PostgreSQL database:**

  - Make sure PostgreSQL is running.
  - Create a database (e.g., `mini_food_db`).
  - Update your `.env` or configuration to point to this database.

  6. **Run database migrations:**

  ```bash
  flask db upgrade
  ```

  7. **Start the Flask server:**

  ```bash
  flask run
  ```

  8. **Access the API:**

  - The API will be available at `http://localhost:5000/`.

  ***

This project is a Flask-based backend for a food recommendation system, using PostgreSQL as the database and SQLAlchemy for ORM. It is containerized with Docker for easy deployment.

## Available Routes

### General

- `GET /` — Returns a welcome message.

### Persons

- `GET /persons` — Retrieve a list of all persons.
  **Response:**
  ```json
  [
    { "id": 1, "name": "Alice", "age": 25 },
    { "id": 2, "name": "Bob", "age": 30 }
  ]
  ```
- `POST /persons` — Create a new person.
  **Request Body:**
  ```json
  {
    "name": "John Doe",
    "age": 28
  }
  ```
  **Response:**
  ```json
  {
    "id": 3,
    "name": "John Doe",
    "age": 28
  }
  ```
- `GET /persons/<person_id>` — Retrieve details of a specific person by ID.
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Alice"
  }
  ```
- `PUT /persons/<person_id>` — Update a person's name.
  **Request Body:**
  ```json
  {
    "name": "Alice Smith"
  }
  ```
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Alice Smith"
  }
  ```
- `DELETE /persons/<person_id>` — Delete a person by ID.
  **Response:**
  ```json
  {
    "message": "Person deleted successfully"
  }
  ```
- `GET /persons/search?query=<name>` — Search for persons by name (case-insensitive, partial match).
  **Response:**
  ```json
  [{ "id": 1, "name": "Alice" }]
  ```
- `GET /persons/<person_id>/foods` — Get all foods associated with a person.
  **Response:**
  ```json
  [
    { "id": 1, "name": "Pizza" },
    { "id": 2, "name": "Salad" }
  ]
  ```
- `POST /persons/<person_id>/foods/<food_id>` — Add a food to a person's list.
  **Response:**
  ```json
  {
    "message": "Food added to person successfully"
  }
  ```
- `DELETE /persons/<person_id>/foods/<food_id>` — Remove a food from a person's list.
  **Response:**
  ```json
  {
    "message": "Food removed from person successfully"
  }
  ```
- `PUT /persons/<person_id>/foods/<food_id>` — Update the name of a food associated with a person.
  **Request Body:**
  ```json
  {
    "name": "New Food Name"
  }
  ```
  **Response:**
  ```json
  {
    "id": 1,
    "name": "New Food Name"
  }
  ```

### Foods

- `GET /foods` — List all foods.
  **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Pizza",
      "ingredients": ["Cheese", "Tomato"]
    },
    {
      "id": 2,
      "name": "Salad",
      "ingredients": ["Lettuce", "Tomato"]
    }
  ]
  ```
- `POST /foods` — Create a new food.
  **Request Body:**
  ```json
  {
    "name": "Burger",
    "ingredients": ["Beef", "Cheese"]
  }
  ```
  **Response:**
  ```json
  {
    "id": 3,
    "name": "Burger"
  }
  ```
- `GET /foods/<food_id>` — Get details of a specific food.
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Pizza",
    "ingredients": ["Cheese", "Tomato"]
  }
  ```
- `PUT /foods/<food_id>` — Update a food's name and ingredients.
  **Request Body:**
  ```json
  {
    "name": "Veggie Pizza",
    "ingredients": ["Cheese", "Tomato", "Peppers"]
  }
  ```
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Veggie Pizza"
  }
  ```
- `DELETE /foods/<food_id>` — Delete a food.
  **Response:**
  ```json
  {
    "message": "Food deleted successfully"
  }
  ```
- `GET /foods/search?query=<name>` — Search for foods by name (case-insensitive, partial match).
  **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Pizza",
      "ingredients": ["Cheese", "Tomato"]
    }
  ]
  ```
- `GET /foods/<food_id>/ingredients` — Get all ingredients for a specific food.
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Pizza",
    "ingredients": ["Cheese", "Tomato"]
  }
  ```
- `POST /foods/<food_id>/ingredients` — Add an ingredient to a food.
  **Request Body:**
  ```json
  {
    "name": "Olives"
  }
  ```
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Pizza",
    "ingredients": ["Cheese", "Tomato", "Olives"]
  }
  ```
- `DELETE /foods/<food_id>/ingredients/<ingredient_id>` — Remove an ingredient from a food.
  **Response:**
  ```json
  {
    "message": "Ingredient removed from food successfully"
  }
  ```
- `PUT /foods/<food_id>/ingredients/<ingredient_id>` — Update the name of an ingredient in a food.
  **Request Body:**
  ```json
  {
    "name": "Mozzarella"
  }
  ```
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Pizza",
    "ingredients": ["Mozzarella", "Tomato"]
  }
  ```
- `GET /foods/<food_id>/ingredients/<ingredient_id>` — Get details of a specific ingredient in a food.
  **Response:**
  ```json
  {
    "id": 2,
    "name": "Tomato"
  }
  ```
- `GET /foods/<food_id>/ingredients/<ingredient_id>/exists` — Check if an ingredient exists in a food.
  **Response:**
  ```json
  {
    "exists": true
  }
  ```
- `GET /foods/<food_id>/ingredients/<ingredient_id>/count` — Get the count of a specific ingredient in a food (usually 1 or 0).
  **Response:**
  ```json
  {
    "count": 1
  }
  ```
- `PUT /foods/<food_id>/ingredients/<ingredient_id>/update` — Update ingredient details in a food.
  **Request Body:**
  ```json
  {
    "name": "Red Tomato"
  }
  ```
  **Response:**
  ```json
  {
    "id": 1,
    "name": "Pizza",
    "ingredients": ["Cheese", "Red Tomato"]
  }
  ```
- `DELETE /foods/<food_id>/ingredients/<ingredient_id>/delete` — Remove an ingredient from a food.
  **Response:**
  ```json
  {
    "message": "Ingredient removed from food successfully"
  }
  ```

### Ingredients

- `GET /ingredients` — List all ingredients.
- `GET /ingredients/<id>` — Get details of a specific ingredient.
- `POST /ingredients` — Create a new ingredient.
  **Body:**
  ```json
  {
    "name": "Tomato"
  }
  ```
- `PUT /ingredients/<id>` — Update an ingredient.
  **Body:**
  ```json
  {
    "name": "Cheese"
  }
  ```
- `DELETE /ingredients/<id>` — Delete an ingredient.

### Food Consumption

- `GET /consumptions` — List all food consumption records.
  **Response:**
  ```json
  [
    {
      "id": 1,
      "user_id": 1,
      "food_id": 2,
      "timestamp": "2025-06-11T12:00:00"
    }
  ]
  ```
- `GET /consumptions/<id>` — Get details of a specific consumption record.
  **Response:**
  ```json
  {
    "id": 1,
    "user_id": 1,
    "food_id": 2,
    "timestamp": "2025-06-11T12:00:00"
  }
  ```
- `POST /consumptions` — Add a new food consumption record.
  **Request Body:**
  ```json
  {
    "person_id": 1,
    "food_id": 2
  }
  ```
  **Response:**
  ```json
  {
    "id": 1,
    "user_id": 1,
    "food_id": 2,
    "timestamp": "2025-06-11T12:00:00"
  }
  ```
- `PUT /consumptions/<id>` — Update a food consumption record.
  **Request Body:**
  ```json
  {
    "user_id": 1,
    "food_id": 3,
    "timestamp": "2025-06-12T14:00:00"
  }
  ```
- `DELETE /consumptions/<id>` — Delete a food consumption record.
  **Response:**
  ```json
  {
    "message": "Food consumption deleted successfully"
  }
  ```
- `GET /consumptions/person/<person_id>` — List all consumption records for a specific person.
  **Response:**
  ```json
  [
    {
      "id": 1,
      "user_id": 1,
      "food_id": 2,
      "timestamp": "2025-06-11T12:00:00"
    }
  ]
  ```
- `GET /consumptions/food/<food_id>` — List all consumption records for a specific food.
  **Response:**
  ```json
  [
    {
      "id": 1,
      "user_id": 1,
      "food_id": 2,
      "timestamp": "2025-06-11T12:00:00"
    }
  ]
  ```
- `GET /consumptions/person/<person_id>/food/<food_id>` — Get a specific consumption record for a person and food.
  **Response:**
  ```json
  {
    "id": 1,
    "user_id": 1,
    "food_id": 2,
    "timestamp": "2025-06-11T12:00:00"
  }
  ```
- `POST /consumptions/person/<person_id>/food/<food_id>` — Add a consumption record for a person and food.
  **Response:**
  ```json
  {
    "id": 1,
    "user_id": 1,
    "food_id": 2,
    "timestamp": "2025-06-11T12:00:00"
  }
  ```
- `DELETE /consumptions/person/<person_id>/food/<food_id>` — Delete a consumption record for a person and food.
  **Response:**
  ```json
  {
    "message": "Food consumption deleted successfully"
  }
  ```
- `GET /consumptions/person/<person_id>/foods` — List all foods consumed by a person.
  **Response:**
  ```json
  [
    { "id": 1, "name": "Pizza" },
    { "id": 2, "name": "Salad" }
  ]
  ```

### Food Images

- `GET /foods/<food_id>/images` — List images for a food.
- `POST /foods/<food_id>/images` — Upload an image for a food (multipart/form-data).
- `DELETE /foods/<food_id>/images/<image_id>` — Delete a specific image for a food.

### Food Recommendation Routes

- `GET /recommendations/<person_id>` — Get food recommendations for a specific person.
  **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Pizza",
      "score": 0.95
    },
    {
      "id": 2,
      "name": "Salad",
      "score": 0.89
    }
  ]
  ```
  - Returns a list of recommended foods for the given person, possibly with a score or ranking.
  - If the person does not exist, returns:
  ```json
  { "error": "Person not found" }
  ```

---

### Allergy Probability Routes

- `GET /allergy_probability/<person_id>/<food_id>` — Get the probability that a person is allergic to a specific food.
  **Response:**
  ```json
  {
    "probability": 0.23
  }
  ```
  - Returns a probability value (between 0 and 1) indicating the likelihood of an allergy.
  - If an error occurs, returns:
  ```json
  { "error": "Error message" }
  ```

---

## Weekly Plan Routes

- `POST /weekly_plan/<person_id>` — Set or update a person's weekly food plan.
  **Request Body:**

  ```json
  {
    "plan": {
      "Monday": [1, 2],
      "Tuesday": [3],
      "Wednesday": [],
      "Thursday": [4],
      "Friday": [5],
      "Saturday": [],
      "Sunday": [6]
    }
  }
  ```

  (Where numbers are food IDs.)
  **Response:**

  ```json
  { "message": "Weekly plan set successfully" }
  ```

- `GET /weekly_plan/<person_id>` — Retrieve a person's weekly food plan.
  **Response:**

  ```json
  {
    "person_id": 1,
    "plan": {
      "Monday": [
        { "food_id": 1, "food_name": "Pizza" },
        { "food_id": 2, "food_name": "Salad" }
      ],
      "Tuesday": [{ "food_id": 3, "food_name": "Burger" }]
      // ... other days
    }
  }
  ```

- `DELETE /weekly_plan/<person_id>` — Delete a person's weekly food plan.
  **Response:**
  ```json
  { "message": "Weekly plan deleted successfully" }
  ```

---

### Buffet Management Routes

- `POST /buffet`— Create a buffet plan for an event.
  **Request Body:**

  ```json
  {
    "event_name": "Birthday Party",
    "guest_count": 50,
    "food_ids": [1, 2, 3]
  }
  ```

  **Response:**

  ```json
  { "message": "Buffet plan created", "buffet_id": 1 }
  ```

- `GET /buffet` — Get list of all buffet planned.
  **Response:**

  ```json
  [
    {
      "buffet_id": 1,
      "event_name": "Event 1",
      "foods": [
        {
          "food_id": 97,
          "food_name": "Food 47",
          "servings": 52
        },
        {
          "food_id": 93,
          "food_name": "Food 43",
          "servings": 52
        }
      ],
      "guest_count": 52
    }
  ]
  ```

- `GET /buffet/<buffet_id>` — Retrieve a buffet plan by its ID.
  **Response:**

  ```json
  {
    "event_name": "Birthday Party",
    "guest_count": 50,
    "foods": [
      { "food_id": 1, "food_name": "Pizza", "servings": 50 },
      { "food_id": 2, "food_name": "Salad", "servings": 50 },
      { "food_id": 3, "food_name": "Burger", "servings": 50 }
    ]
  }
  ```

- `DELETE /buffet/<buffet_id>` — Delete a buffet plan by its ID.
  **Response:**
  ```json
  { "message": "Buffet plan deleted successfully" }
  ```
  ***

## Database Model

The Mini Food Recommendation Backend uses the following relational model:

- **Person**

  - `id`: Integer, primary key
  - `name`: String, required
  - `age`: Integer, optional
  - **Relationships:**
    - Many-to-many with Food (favorites)
    - One-to-many with FoodConsumption
    - One-to-many with WeeklyPlan

- **Food**

  - `id`: Integer, primary key
  - `name`: String, required
  - **Relationships:**
    - Many-to-many with Ingredient
    - Many-to-many with Person (favorites)
    - One-to-many with FoodConsumption
    - One-to-many with FoodImage
    - One-to-many with WeeklyPlan
    - One-to-many with BuffetFood

- **Ingredient**

  - `id`: Integer, primary key
  - `name`: String, required
  - **Relationships:**
    - Many-to-many with Food

- **FoodConsumption**

  - `id`: Integer, primary key
  - `user_id`: Foreign key to Person
  - `food_id`: Foreign key to Food
  - `timestamp`: DateTime
  - **Relationships:**
    - Many-to-one with Person
    - Many-to-one with Food

- **FoodImage**

  - `id`: Integer, primary key
  - `food_id`: Foreign key to Food
  - `image_data`: Binary
  - `content_type`: String (e.g., "image/png")
  - **Relationships:**
    - Many-to-one with Food

- **WeeklyPlan**

  - `id`: Integer, primary key
  - `person_id`: Foreign key to Person
  - `day_of_week`: String (e.g., "Monday")
  - `food_id`: Foreign key to Food
  - **Relationships:**
    - Many-to-one with Person
    - Many-to-one with Food

- **BuffetPlan**

  - `id`: Integer, primary key
  - `event_name`: String
  - `guest_count`: Integer
  - `created_at`: DateTime
  - **Relationships:**
    - One-to-many with BuffetFood

- **BuffetFood**
  - `id`: Integer, primary key
  - `buffet_id`: Foreign key to BuffetPlan
  - `food_id`: Foreign key to Food
  - `servings`: Integer
  - **Relationships:**
    - Many-to-one with BuffetPlan
    - Many-to-one with Food

**Associations:**

- `person_food`: Join table for Person and Food (favorites)
- `food_ingredient`: Join table for Food and Ingredient

**Diagram:**

```
Person *---< FoodConsumption >---* Food *---* Ingredient
   |         ^                   |   |         ^
   |         |                   |   |         |
   *---* person_food             |   *---< FoodImage
   |                             |
   *---< WeeklyPlan >---*        *---< BuffetFood >---* BuffetPlan
```

- `*---*` = many-to-many
- `*---<` = one-to-many

This schema supports user profiles, foods, ingredients, consumption history, food images, weekly meal planning, buffet management, and recommendations.

---

## Notes

- All endpoints return JSON responses.
- Make sure to run migrations before using the API.
- For development, you can modify and extend the routes in the `mini_food_recommendation_backend` package.

---

## Author Information

- Name: ALHADJI OUMATE
- Student ID: 22U2033

## License

This project is for educational purposes.
