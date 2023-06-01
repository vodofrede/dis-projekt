import dotenv
import flask
import route

# load .env file into environment
dotenv.load_dotenv()
dotenv.load_dotenv(".env.example")

# initialize app and db connection
app = flask.Flask(
    __name__, 
    static_url_path="/assets", 
    static_folder="../assets", 
    template_folder="../templates"
)
app.instance_path = "./"

# todo: load models / init db connection

# load route blueprints
app.register_blueprint(route.root)
