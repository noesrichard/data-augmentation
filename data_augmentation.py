from block import Block
from row import Row
from table import Table
import random

class DataAugmentator: 

    def __init__(self, table: Table, window_size: int) -> None:
        self.table: Table = table
        self.window_size: int = window_size
        self.blocks:list[Block] = []

    def print_table(self) -> None: 
        self.table.print()

    def print_blocks(self) -> None: 
        for block in self.blocks: 
            block.print()

    def random_mix(self) -> None: 
        random.shuffle(self.table.rows)

    def split_into_blocks(self) -> None: 
        items_for_block = int(self.table.len()/self.window_size)

        block_jump = 0

        for i in range(0,items_for_block): 
            block: Block = Block(self.table.rows[block_jump:block_jump+self.window_size], i+1)
            self.blocks.append(block)
            block_jump+=self.window_size
    

    def insert_random_values(self) -> None: 
        for block in self.blocks: 
            block.print()
            new_rows = self.__create_random_rows(block)
            print(new_rows)
            block.append_rows(new_rows)

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
        new_row: Row = Row(**row.serialize());

        new_row.ingredient_id = random.randrange(1,100)

        new_row.value = int(random.uniform(start, stop))

        return new_row
        



