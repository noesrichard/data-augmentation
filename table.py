from row import Row


class Table:

    def __init__(self, rows: list[Row]) -> None:
        self.rows: list[Row] = rows

    def print(self) -> None:
        for row in self.rows:
            print(row.serialize())

    def len(self) -> int:
        return len(self.rows)

    def is_created(self, id) -> bool:
        if id in [row.id for row in self.rows]:
            return True
        return False

