# Ecommerce REST API

This is a comprehensive ecommerce REST API built with Django and Django Rest Framework (DRF). The API provides endpoints for managing products, collections, reviews, carts, cart items, customers, orders, and product images. The application utilizes advanced developer tools like Locust for load testing, Silk for performance profiling, and Flower for monitoring Celery tasks.

## Features

- **Product Management**: Create, retrieve, update, and delete products. Products can be filtered, searched, and ordered by various fields.

- **Collection Management**: Manage collections of products. Collections are annotated with the number of products they contain.

- **Review Management**: Manage reviews for products. Reviews are filtered by the product they are associated with.

- **Cart Management**: Create, retrieve, and delete carts. Carts include their items and associated products.
Cart Item Management: Manage items within a cart, including adding, updating, and deleting items.

- **Customer Management**: Manage customer profiles and view customer order history.
Order Management: Create, retrieve, update, and delete orders. Orders are associated with customers and products.

- **Product Image Management**: Manage images associated with products.


## Tools and Technologies

- **Django**: High-level Python web framework.
- **Django Rest Framework (DRF)**: Powerful and - **flexible toolkit for building Web APIs.
- **Django Filters**: Simplifies complex queries and - **e**nables filtering of querysets.
- **Locust**: Open source load testing tool.
- **Silk**: Live profiling and inspection of Django - **projects.
- **Celery**: Distributed task queue.
- **Flower**: Real-time monitor for Celery.

## Swagger Documentation

To explore and test the API endpoints, visit the Swagger documentation at [http://localhost:8000/swagger/schema](http://localhost:8000/swagger/schema). This interactive documentation provides detailed information about each endpoint, including the expected request bodies, response formats, and query parameters.




## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gurjika/DRF-store-backend.git
    ```

2. Change into the project directory:
    ```sh
    cd storefront3
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


5. Create a superuser:
    ```sh
    docker-compose run django python manage.py createsuperuser
    ```

6. Access the development server at [http://localhost:8000](http://localhost:8000).

With these steps, your CulinaryApp should be up and running using Docker Compose. Enjoy exploring and managing your favorite dishes!
