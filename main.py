from data_augmentation import MealIngredientDataAugmentator
from row import MealIngredientsRow, IngredientRow, Row
from table import Table
from connection import Connection

if __name__ == "__main__":
    connection = Connection();

    # Ingredientes
    data = connection.query_as_dict("SELECT id, name FROM ingredients")
    ingredients: Table = Table([IngredientRow(**data) for data in data])

    # Generacion de la tabla meal_ingredients
    data = connection.query_as_dict("SELECT id, meal_id, ingredient_id, quantity FROM meal_ingredients")
    table: Table = Table([MealIngredientsRow(**data) for data in data])

    # Instanciacion del aumentador de datos
    data_augmentator: MealIngredientDataAugmentator = MealIngredientDataAugmentator(connection,table, 10, ingredients)

    # Mix randomico del orden de las filas
    data_augmentator.random_mix()

    data_augmentator.split_into_blocks()

    data_augmentator.print_blocks()

    data_augmentator.insert_random_rows()
