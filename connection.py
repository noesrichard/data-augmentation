import pyodbc
from row import MealIngredientsRow
from table import Table


class Connection:

    def __init__(self) -> None:
        self.connection = pyodbc.connect('''Driver={ODBC Driver 17 for SQL server};
                Server=localhost;
                Database=restaurants;
                Trusted_Connection=yes;''')
        self.cursor = self.connection.cursor()

    def query(self, query: str):
        return self.cursor.execute(query)

    def insert(self, sql: str):
        self.cursor.execute(sql)
        self.cursor.commit()

    def query_as_dict(self, query: str) -> list[dict]:
        self.cursor.execute(query)
        columns = [column[0] for column in self.cursor.description]
        results = []
        for table_row in self.cursor.fetchall():
            results.append(dict(zip(columns, table_row)))
        return results
