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

To explore and test the API endpoints, visit the Swagger documentation at [http://localhost:8000/swagger/schema](http://localhost:8000/swagger/schema). This interactive documentation provides detailed information about each endpoint, including the expected request bodies, response formats, and query parameters.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gurjika/culinaryapp-api.git
    ```

2. Change into the project directory:
    ```sh
    cd culinaryapp-api
    ```

3. Create a `.env` file and specify the required environment variables:
    ```env
    PASSWORD=your_db_password
    HOST=mysql
    ```

4. Run the application using Docker Compose:
    ```sh
    docker-compose up -d
    ```

5. Run the database migrations:
    ```sh
    docker-compose run django python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    docker-compose run django python manage.py createsuperuser
    ```

7. Access the development server at [http://localhost:8000](http://localhost:8000).

With these steps, your CulinaryApp should be up and running using Docker Compose. Enjoy exploring and managing your favorite dishes!
