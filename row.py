class Row:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")

    def serialize(self):
        return {"id": self.id}


class IngredientRow(Row):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name")

    def serialize(self):
        return {**super().serialize(),
                "name": self.name
                }


class MealIngredientsRow(Row):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.meal_id = kwargs.get("meal_id")
        self.ingredient_id = kwargs.get("ingredient_id")
        self.value = kwargs.get("quantity")

    def serialize(self) -> dict:
        return {**super().serialize(),
                "meal_id": self.meal_id,
                "ingredient_id": self.ingredient_id,
                "quantity": self.value
                }

    def __repr__(self) -> str:
        return f"[id: {self.id}; meal_id: {self.meal_id}; ingredient_id: {self.ingredient_id}; quantity: {self.value}]\n"
