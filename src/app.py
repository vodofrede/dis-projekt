
import dotenv
import flask
from route import blueprint

# load .env file into environment
dotenv.load_dotenv()
dotenv.load_dotenv(".env.example")

# initialize app and db connection
app = flask.Flask(__name__)
app.instance_path = "./"

# todo: load models / init db connection
# todo

# load route blueprints
app.register_blueprint(blueprint)
