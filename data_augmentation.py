from block import Block
from connection import Connection
from row import IngredientRow, MealIngredientsRow, Row
from table import Table
import random


class DataAugmentator:
    def __init__(self, connection: Connection, table: Table, window_size: int) -> None:
        self.connection = connection
        self.table: Table = table
        self.window_size: int = window_size
        self.blocks: list[Block] = []

    def print_table(self) -> None:
        self.table.print()

    def print_blocks(self) -> None:
        for block in self.blocks:
            block.print()

    def random_mix(self) -> None:
        random.shuffle(self.table.rows)

    def split_into_blocks(self) -> None:
        items_for_block = int(self.table.len() / self.window_size)
        # block_jump divide desde n hasta n + el tamaño de ventana o tamaño del bloque
        block_jump = 0
        for i in range(0, items_for_block):
            block: Block = Block(self.table.rows[block_jump:block_jump + self.window_size], i + 1)
            self.blocks.append(block)
            block_jump += self.window_size


class MealIngredientDataAugmentator(DataAugmentator):

    def __init__(self, connection: Connection, table: Table, window_size: int, ingredients: Table) -> None:
        super().__init__(connection, table, window_size)
        self.ingredients: Table = ingredients

    def insert_random_rows(self) -> None:
        for block in self.blocks:
            new_rows = self.__create_random_rows(block)

    def __create_random_rows(self, block: Block) -> list[Row]:
        new_rows: list[Row] = []
        max_value = block.max()
        min_value = block.min()
        mean = block.mean()
        median = block.median()
        for row in block.rows:
            new_rows.append(self.__create_random_row(row, min_value, max_value))

        for row in block.rows:
            new_rows.append(self.__create_random_row(row, mean, median))
        return new_rows

    def __create_random_row(self, row, start, stop):
        new_row: MealIngredientsRow = MealIngredientsRow(**row.serialize());

        new_row.ingredient_id = random.randrange(1, 100)

        while self.__ingredient_created(new_row.ingredient_id) and len(self.ingredients.rows) < 100:
            new_row.ingredient_id = random.randrange(1, 101)

        new_row.value = int(random.uniform(start, stop))

        if not self.__ingredient_created(new_row.ingredient_id):
            self.__insert_new_ingredient(new_row.ingredient_id)

        return new_row

    def __insert_new_ingredient(self, ingredient_id: int):
        self.ingredients.rows.append(IngredientRow(id=ingredient_id, name=f"Ingredient {ingredient_id}"))
        self.connection.insert(f"INSERT INTO ingredients values({ingredient_id},'Ingredient {ingredient_id}')")

    def __ingredient_created(self, new_id: int) -> bool:
        if new_id in [ingredient.id for ingredient in self.ingredients.rows]:
            return True
        return False
