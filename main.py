from data_augmentation import DataAugmentator
from row import MealIngredientsRow, IngredientRow, Row
from table import Table
from connection import Connection

if __name__ == "__main__":
    # Conexion a la base de datos
    connection = Connection();

    # Generacion de la tabla de engredientes
    data = connection.query_as_dict("SELECT id, name FROM ingredients")
    ingredients: Table = Table([IngredientRow(**data) for data in data])

    # Generacion de la tabla meal_ingredients
    data = connection.query_as_dict("SELECT id, meal_id, ingredient_id, quantity FROM meal_ingredients")
    table: Table = Table([MealIngredientsRow(**data) for data in data])

    # Instanciacion del aumentador de datos
    data_augmentator: DataAugmentator = DataAugmentator(connection, table, 10, ingredients)

    # Mix randomico del orden de las filas
    data_augmentator.random_mix()

    # Dividir la tabla en bloques
    data_augmentator.split_into_blocks()

    # Generacion de filas con datos aleatorios
    data_augmentator.create_random_rows()

