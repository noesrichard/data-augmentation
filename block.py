from row import Row
from table import Table
from statistics import mean, median

class Block(Table): 

    def __init__(self, rows: list[Row], id) -> None:
        super().__init__(rows)
        self.id = id


    def max(self) -> float: 
       return max(row.value for row in self.rows) 

    def min(self) -> float: 
       return min(row.value for row in self.rows) 
        

    def mean(self) -> float: 
        return mean(row.value for row in self.rows)

    def median(self) -> float: 
        return median(row.value for row in self.rows)

    def print(self) -> None: 
        print(f'''\n\nBloque numero: {self.id} \tMax Value: {self.max()} \tMin Value: {self.min()} \tMedia: {self.mean()} \tMediana: {self.median()}\n''')
        super().print()

    def append_rows(self, rows) -> None: 
        self.rows += rows






