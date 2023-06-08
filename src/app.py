import os

import dotenv
import flask
import route
import user

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

# initialize login manager
app.secret_key = os.environ["APP_SECRET_KEY"] 
print(f"Secret key is {app.secret_key}")
user.login_manager.init_app(app)

# load route blueprints
app.register_blueprint(route.root)
