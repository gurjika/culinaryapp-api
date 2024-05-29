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
- **Chef Profiles**: Users can view and follow their favorite chefs.

## Models

### UserProfile
- `user`: One-to-one relationship with the `User` model.

### Ingredient
- `title`: CharField for the name of the ingredient.

### Dish
- `title`: CharField for the name of the dish.
- `profile`: ForeignKey to the `UserProfile` model.
- `receipe`: TextField for the dish's recipe.
- `ingredient`: Many-to-many relationship with the `Ingredient` model through `DishIngredient`.

### DishIngredient
- `ingredient`: ForeignKey to the `Ingredient` model.
- `dish`: ForeignKey to the `Dish` model.
- `quantity`: FloatField for the quantity of the ingredient.
- `quantity_description`: CharField for the description of the quantity.

### DishImage
- `dish`: ForeignKey to the `Dish` model.
- `image`: ImageField for the dish's image.

### ChefProfile
- `name`: CharField for the chef's first name.
- `last_name`: CharField for the chef's last name.
- `specialty`: CharField for the chef's specialty.
- `bio`: TextField for the chef's biography.
- `profile`: ForeignKey to the `UserProfile` model.

### Rating
- `rating`: FloatField for the rating with validators for max and min values.
- `dish`: ForeignKey to the `Dish` model.
- `profile`: ForeignKey to the `UserProfile` model.

### DishTypeTag
- `dish`: Many-to-many relationship with the `Dish` model through `DishTag`.
- `dish_tag`: CharField for the tag name.

### DishTag
- `dish`: ForeignKey to the `Dish` model.
- `tag`: ForeignKey to the `DishTypeTag` model.

### FavouriteDish
- `profile`: ForeignKey to the `UserProfile` model.
- `dish`: ForeignKey to the `Dish` model.

## API Endpoints

### User
- `GET /users/`: List all users.
- `POST /users/`: Create a new user.
- `GET /users/{id}/`: Retrieve a user by ID.
- `PUT /users/{id}/`: Update a user by ID.
- `DELETE /users/{id}/`: Delete a user by ID.

### Dish
- `GET /dishes/`: List all dishes.
- `POST /dishes/`: Create a new dish.
- `GET /dishes/{id}/`: Retrieve a dish by ID.
- `PUT /dishes/{id}/`: Update a dish by ID.
- `DELETE /dishes/{id}/`: Delete a dish by ID.

### Ingredient
- `GET /ingredients/`: List all ingredients.
- `POST /ingredients/`: Create a new ingredient.
- `GET /ingredients/{id}/`: Retrieve an ingredient by ID.
- `PUT /ingredients/{id}/`: Update an ingredient by ID.
- `DELETE /ingredients/{id}/`: Delete an ingredient by ID.

### Rating
- `GET /ratings/`: List all ratings.
- `POST /ratings/`: Create a new rating.
- `GET /ratings/{id}/`: Retrieve a rating by ID.
- `PUT /ratings/{id}/`: Update a rating by ID.
- `DELETE /ratings/{id}/`: Delete a rating by ID.

### FavouriteDish
- `GET /favourites/`: List all favourite dishes.
- `POST /favourites/`: Create a new favourite dish.
- `GET /favourites/{id}/`: Retrieve a favourite dish by ID.
- `DELETE /favourites/{id}/`: Delete a favourite dish by ID.

### ChefProfile
- `GET /chefs/`: List all chefs.
- `POST /chefs/`: Create a new chef profile.
- `GET /chefs/{id}/`: Retrieve a chef profile by ID.
- `PUT /chefs/{id}/`: Update a chef profile by ID.
- `DELETE /chefs/{id}/`: Delete a chef profile by ID.

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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
"""