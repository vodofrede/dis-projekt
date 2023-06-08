import flask
import flask_login
import model

# subroutes
import recipe
import user

# register subroutes
root = flask.Blueprint("app", __name__)
# root.register_blueprint(ingredient.ingredient)
root.register_blueprint(recipe.recipe)
root.register_blueprint(user.blueprint)


# root
@root.route("/")
def front():
    print(flask_login.current_user)
    return flask.render_template(
        "frontpage.html",
        title="Recipes",
        user=flask_login.current_user,
        recipes=model.Recipe.get_all_recipes(),
    )
