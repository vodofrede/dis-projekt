import flask
import flask_login
import model
from user import User

recipe = flask.Blueprint("recipe", __name__)


# render add recipe site
@recipe.route("/addrecipe", methods=["GET"])
@flask_login.login_required
def getAddRecipePage():
    return flask.render_template(
        "addrecipe.html", title="Add Recipe", user=flask_login.current_user
    )


# render add recipe site
@recipe.route("/recipe/<int:id>", methods=["GET"])
def getRecipePage(id):
    recipe = model.Recipe.getRecipeById(id)
    return flask.render_template(
        "recipepage.html", title="Recipe", user=flask_login.current_user, recipe=recipe
    )


# add recipe
@recipe.route("/addrecipe", methods=["POST"])
@flask_login.login_required
def createRecipe():
    name = flask.request.form["name"]
    category = flask.request.form["category"]
    cuisine = flask.request.form["cuisine"]
    ingredients = flask.request.form["ingredients"]
    description = flask.request.form["description"]
    method = flask.request.form["method"]
    currentUser = User.get_user(flask_login.current_user.id).user_id
    recipe = [name, category, cuisine, ingredients, description, method, currentUser]

    recipeCreated = model.Recipe.addRecipe(recipe)
    print(recipeCreated)

    return flask.redirect(flask.url_for("app.front"), code=302)


# delete recipe
@recipe.route("/deleterecipe", methods=["POST"])
@flask_login.login_required
def deleteRecipe():
    recipeId = flask.request.form["id"]
    currentUserId = User.get_user(flask_login.current_user.id).user_id

    dbRecipe = model.Recipe.getRecipeById(recipeId)

    if dbRecipe.created_by == currentUserId:
        model.Recipe.deleteRecipe(recipeId)
        return flask.redirect(flask.url_for("app.front"), code=302)
    else:
        return flask.abort(401)
