
class Row: 

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.meal_id = kwargs.get("meal_id")
        self.ingredient_id = kwargs.get("ingredient_id")
        self.value = kwargs.get("quantity")


    def serialize(self) -> dict: 
        return { "id": self.id,
                 "meal_id": self.meal_id,
                 "ingredient_id": self.ingredient_id,
                 "quantity": self.value
                }
       

    def __repr__(self) -> str:
        return f"[id: {self.id}; meal_id: {self.meal_id}; ingredient_id: {self.ingredient_id}; quantity: {self.value}]\n"

