from block import Block
from connection import Connection
from row import IngredientRow, MealIngredientsRow, Row
from table import Table
import random


class DataAugmentator:

    def __init__(self, connection: Connection, table: Table, window_size: int, ingredients: Table) -> None:
        self.connection = connection
        self.table: Table = table
        self.window_size: int = window_size
        self.blocks: list[Block] = []
        self.ingredients: Table = ingredients

    def random_mix(self) -> None:
        random.shuffle(self.table.rows)

    def split_into_blocks(self) -> None:
        items_for_block = int(self.table.len() / self.window_size)
        # block_jump divide desde n hasta (n + el tamaño de ventana o tamaño del bloque)
        block_jump = 0
        for i in range(0, items_for_block):
            block: Block = Block(self.table.rows[block_jump:block_jump + self.window_size], i + 1)
            self.blocks.append(block)
            block_jump += self.window_size

    def create_random_rows(self) -> None:
        for block in self.blocks:
            for row in block.rows:
                self.__create_random_row(row, block.min(), block.max())
                self.__create_random_row(row, block.mean(), block.median())

    def __create_random_row(self, row, start, stop) -> None:
        new_row: MealIngredientsRow = MealIngredientsRow(**row.serialize())

        new_row.ingredient_id = random.randrange(1, 101)
        new_row.value = int(random.uniform(start, stop))

        while self.__ingredient_not_valid(new_row.ingredient_id):
            new_row.ingredient_id = random.randrange(1, 101)

        if not self.ingredients.is_created(new_row.ingredient_id):
            self.__insert_new_ingredient(new_row.ingredient_id)

        self.__insert_new_row(new_row)

    def __ingredient_not_valid(self, ingredient_id):
        if self.ingredients.is_created(ingredient_id) and len(self.ingredients.rows) < 100:
            return True
        return False

    def __insert_new_row(self, row):
        self.connection.insert(f'''INSERT INTO meal_ingredients(meal_id, ingredient_id, quantity) 
                                    VALUES ({row.meal_id},{row.ingredient_id},{row.value});''')

    def __insert_new_ingredient(self, ingredient_id: int) -> None:
        self.ingredients.rows.append(IngredientRow(id=ingredient_id, name=f"Ingredient {ingredient_id}"))
        self.connection.insert(f"INSERT INTO ingredients values({ingredient_id},'Ingredient {ingredient_id}')")

    def print_table(self) -> None:
        self.table.print()

    def print_blocks(self) -> None:
        for block in self.blocks:
            block.print()



