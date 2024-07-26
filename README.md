# CulinaryApp

CulinaryApp is a Django-based web application that allows users to create, manage, and explore various dishes. Users can rate dishes, add ingredients, upload images, and follow their favorite chefs. The application leverages Django Rest Framework for creating APIs and includes models for dishes, ingredients, ratings, and user profiles.

## Features

- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Dish Management**: Users can create, update, and delete dishes.
- **Ingredient Management**: Users can add and remove ingredients for dishes.
- **Image Upload**: Users can upload images for their dishes.
- **Rating System**: Users can rate dishes.
- **Favorite Dishes**: Users can add dishes to their favorites.
- **Chef Profiles**: Users can view and add their favorite chefs.
- **Explore Dishes**: Users can explore dishes based on their preferences.


## Tools and Technologies
- **Django Rest Framework**: Provides a powerful and flexible toolkit for building Web APIs.
- **MySQL**: A relational database management system used to store application data.
- **Gunicorn**: A WSGI HTTP server for UNIX used to serve the Django application.

- **Nginx**: A high-performance web server and reverse proxy server.
- **Docker**: Containerization platform used to package the application and its dependencies.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.
- **CI/CD**: Continuous Integration and Continuous Deployment processes for automating the testing and deployment of the application.
- **S3 Bucket and CloudFront**: Used to host media files, leveraging S3 for storage and CloudFront for content delivery.

## Swagger Documentation

To explore and test the API endpoints, visit the Swagger documentation at [http://207.154.236.26/swagger/schema](http://207.154.236.26/swagger/schema). This interactive documentation provides detailed information about each endpoint, including the expected request bodies, response formats, and query parameters.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gurjika/culinaryapp-api.git
    ```

2. Change into the project directory:
    ```sh
    cd culinaryapp-api
    ```

3. Create a `.env` file and specify the required environment variables (Also include AWS credentials):
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

7. Access the development server at [http://localhost](http://localhost).

With these steps, your CulinaryApp should be up and running using Docker Compose. Enjoy exploring and managing your favorite dishes!
