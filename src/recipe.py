from flask import Blueprint, render_template

recipe = Blueprint('recipe', __name__, url_prefix="/recipe")


# get all recipes, filtered or not
@recipe.route("/")
def getAll(count): # define and include type on param?
    recipes = selectAllRecipes(count)
    return render_template('frontpage.html', title='Recipes', recipeList=recipes)

# get all recipes, 
@recipe.route("/")
def get(): # define and include type on param?
    recipes = selectAllRecipes()
    return render_template('frontpage.html', title='Recipes', recipeList=recipes)

# search for recipes, based on ingredient filter (list of ingredients)
@recipe.route("/filter")
def filter(filter):
    recipes = getRecipesByFilter(filter)
    return render_template('frontpage.html', title='Search', recipeList=recipes)

# search for recipe name, return list of hits
@recipe.route("/search")
def search(name):
    recipes = searchRecipes(name)
    return render_template('frontpage.html', title='Search', recipeList=recipes)

# get recipe by id
@recipe.route("/<int:id>")
def getRecipe(id):
    recipe = selectRecipeById(id)
    return render_template('recipesite.html', title='Recipe', recipe=recipe)