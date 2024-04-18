from lib.recipe import *

def test_recipe_construct():
    recipe = Recipe("Cake", 30, 3)
    assert recipe.name == "Cake"
    assert recipe.cooking_time == 30
    assert recipe.rating == 3

"""
we need to compare the recipes to see if there are equal 
"""

def test_recipes_are_equal():
    recipe1 = Recipe("Cake", 30, 3)
    recipe2 = Recipe("Cake", 30, 3)
    assert recipe1 == recipe2

"""
format it nicely
"""

def test_artists_format_nicely():
    recipe = Recipe("Cake", 30, 3)
    assert str(recipe) == "Recipe:Cake, cooking time - 30 minutes, 3"


