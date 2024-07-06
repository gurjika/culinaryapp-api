# CulinaryApp

CulinaryApp is a Django-based web application that allows users to create, manage, and explore various dishes. Users can rate dishes, add ingredients, upload images, and follow their favorite chefs. The application leverages Django Rest Framework for creating APIs and includes models for dishes, ingredients, ratings, and user profiles.

## Features

- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Dish Management**: Users can create, update, and delete dishes.
- **Ingredient Management**: Users can add and remove ingredients for dishes.
- **Image Upload**: Users can upload images for their dishes.
- **Rating System**: Users can rate dishes.
- **Explore Dishes**: Users can explore dishes based on their preferences.
- **Favorite Dishes**: Users can add dishes to their favorites.
- **Chef Profiles**: Users can view and add their favorite chefs.

## Swagger Documentation
To explore and test the API endpoints, visit the Swagger documentation at http://localhost:8000/swagger/schema. This interactive documentation provides detailed information about each endpoint, including the expected request bodies, response formats, and query parameters.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/culinaryapp.git
    ```
2. Change into the project directory:
    ```sh
    cd culinaryapp
    ```
3. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\\Scripts\\activate`
    ```
4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Run the database migrations:
    ```sh
    python manage.py migrate
    ```
6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```
7. Start the development server:
    ```sh
    python manage.py runserver
    ```





