from lib.recipe_repository import *
from lib.recipe import *

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)
    recipes = repository.all()

    assert recipes == [
        Recipe('Cake', 30, 3),
        Recipe('Bread', 60, 4),
        Recipe('Fish', 60, 2),
        Recipe('Potatos', 20, 2)]

def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find('Cake')
    assert recipe == Recipe('Cake', 30, 3)
