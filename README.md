# Mini Food Recommendation Backend

## Table of Contents

- [Getting Started](#getting-started)
  - [System Details](#system-details)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Running on Another Computer](#running-on-another-computer)
  - [Project Execution](#project-execution)

## Getting Started

### System Details

- **OS:** Ubuntu 24.04.2 LTS (or compatible Linux distribution)
- **Database:** PostgreSQL v16
- **Python:** 3.12.3

### Prerequisites

Before running the project, ensure the following are installed:

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- PostgreSQL installed and configured (if running outside Docker)
- Clone this repository to your local machine:
  ```bash
  git clone <repository-url>
  cd <repository-directory>
  ```
- Copy the example environment file and update credentials:
  ```bash
  cp .env.example .env
  # Edit .env to match your database and secret key settings
  ```

### Setup

1. **Build and start the services:**

   ```bash
   docker compose up --build
   ```

   This command builds the Docker images and starts the backend and database containers.

2. **Apply database migrations:**

   ```bash
   docker compose exec web flask db migrate -m 'Description of change'
   docker compose exec web flask db upgrade
   ```

   These commands initialize and apply database schema changes.

3. **(Optional) Seed the database with sample data:**
   ```bash
   docker compose exec web python seed_db.py
   ```
   This step populates the database with initial data for testing.

The backend API will be available at [http://localhost:5000](http://localhost:5000).

- _NB_: make sure you restart the docker execution after migrating the db or populating with sample data.

---

### Running on Another Computer

To run this project on a different machine:

1. **Ensure all prerequisites are installed** (see above).
2. **Clone the repository** to the new machine.
3. **Copy or create the `.env` file** with the correct configuration for the new environment.
4. **Follow the Setup steps** as described above.
5. If using a remote database, update the `.env` file with the appropriate host and credentials.

---

### Project Execution

- After starting the services, you can interact with the backend API at [http://localhost:5000](http://localhost:5000).
- Use tools like [Postman](https://www.postman.com/) or `curl` to test API endpoints.
- Logs from the backend service can be viewed with:
  ```bash
  docker compose logs web
  ```
- To stop the project, press `Ctrl+C` in the terminal running Docker Compose, then run:
  ```bash
  docker compose down
  ```
- For further development, modify the source code and restart the services as needed.

---

## Author Information

- Name: ALHADJI OUMATE
- Student ID: 22U2033
