from lib.recipe import *

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        recipes = []
        for row in rows:
            item = Recipe(row['name'], row['cooking_time'], row['rating'])
            recipes.append(item)
        return recipes
    
    def find(self,name):
        rows = self._connection.execute("SELECT * FROM recipes WHERE name = %s", [name])
        row = rows[0]
        return Recipe(row["name"], int(row["cooking_time"]), int(row["rating"]))