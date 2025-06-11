# Mini Food Recommendation Backend

This project is a Flask-based backend for a food recommendation system, using PostgreSQL as the database and SQLAlchemy for ORM. It is containerized with Docker for easy deployment.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed

### Setup

1. **Build and start the services:**

```bash
docker compose up --build
```

2. **Apply database migrations:**

```bash
docker compose exec web flask db upgrade
```

3. **(Optional) Seed the database with sample data:**

```bash
docker compose exec web python seed_db.py
```

The backend will be available at [http://localhost:5000](http://localhost:5000).

---

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

## Notes

- All endpoints return JSON responses.
- Make sure to run migrations before using the API.
- For development, you can modify and extend the routes in the `mini_food_recommendation_backend` package.

---

## License

This project is for educational purposes.
