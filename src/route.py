import flask

# subroutes
#import ingredient
import recipe
import user

# register subroutes
root = flask.Blueprint("app", __name__)
#root.register_blueprint(ingredient.ingredient)
root.register_blueprint(recipe.recipe)
root.register_blueprint(user.user)

# root
@root.route("/")
def hello():
    return flask.render_template("frontpage.html")
