from connection import Connection
import random

connection = Connection(); 
#insert into meal_ingredients(meal_id, ingredient_id, quantity) values (1, 12, 300);

for i in range(1, 351): 
    for j in range(0, 5): 
        ingredient_id = random.randrange(1,31)
        quantity = random.randrange(100, 501) 
        connection.insert(f"insert into meal_ingredients(meal_id, ingredient_id, quantity) values ({i},{ingredient_id},{quantity});")
        print(f"insert into meal_ingredients(meal_id, ingredient_id, quantity) values ({i},{ingredient_id},{quantity});")
