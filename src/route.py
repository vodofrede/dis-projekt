import flask

blueprint = flask.Blueprint("app", __name__)

# routes
@blueprint.route("/")
def hello():
    return "<p>Hello</p>"
