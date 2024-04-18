from lib.recipe_repository import *
from lib.recipe import *
from lib.database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/recipe_directory.sql")

recipe_repository = RecipeRepository(connection)
recipe = recipe_repository.all()

for recipe in recipe:
    print(recipe)