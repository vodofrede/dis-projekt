import flask
import flask_login
from model import User

# initialize login manager
login_manager = flask_login.LoginManager()

@login_manager.user_loader
def user_loader(username):
    user = User.get_user(username)
    if user is None:
        return
    
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get("username")
    user = User.get_user(username)
    if user is None:
        return

    return user

@login_manager.unauthorized_handler
def unauthorized():
    return 'Unauthorized', 401

# routes
blueprint = flask.Blueprint("user", __name__)

@blueprint.route("/")
def get(id):
    return


@blueprint.route("/about")
def about():
    return flask.render_template("about.html", title="About")


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    """
    Show login page and login user
    """
    if flask.request.method == "GET":
        return flask.render_template("login.html", title="Login")

    username = flask.request.form["username"]
    print(f"got username from login form: {username}")

    # check if user exists
    user = User.get_user(username)
    if user is None:
        return "unknown username"

    print(f"{user.id}, {user.password}")

    # check if password matches
    if flask.request.form["password"] == user.password:
        flask_login.login_user(user)
        return flask.redirect(flask.url_for("app.front"))
    else:
        return "wrong password"


@blueprint.route("/register", methods=["GET", "POST"])
def register():
    """
    Show register user page and register a new user
    """
    # render template if GET
    if flask.request.method == "GET":
        return flask.render_template("register.html", title="Register")

    username = flask.request.form["username"]
    print(f"registering {username}")

    # check if user exists
    user = User.get_user(username)
    if user is not None:
        return "user already exists"

    # register user in database
    user = User.register_user(username, flask.request.form["password"])

    # login the user
    flask_login.login_user(user)

    return flask.redirect(flask.url_for("app.front"))

@blueprint.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("app.front"), code=302)

