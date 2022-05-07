from data_augmentation import DataAugmentator
from row import Row
from table import Table
from connection import Connection
import random

if __name__ == "__main__":
    #Generacion de la tabla
    connection = Connection();
    data = connection.query_as_dict("SELECT id, meal_id, ingredient_id, quantity FROM meal_ingredients")
    rows: list[Row] = [Row(**data) for data in data]
    table = Table(rows)

    #Instanciacion del aumentador de datos
    data_augmentator: DataAugmentator = DataAugmentator(table, 10)


    #Mix randomico del orden de las filas
    data_augmentator.print_table()
    print("RANDOM MIX")
    data_augmentator.random_mix()

    data_augmentator.split_into_blocks()

    data_augmentator.insert_random_values()


