import os

import dotenv
import flask
import flask_migrate
from model import db
from route import blueprint

# load .env file into environment
dotenv.load_dotenv()
dotenv.load_dotenv(".env.example")

# initialize app and db connection
app = flask.Flask(__name__)
app.instance_path = "./"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["APP_DB_URI"]

# load models
migrate = flask_migrate.Migrate(app, db)
db.init_app(app)
with app.app_context():
    db.create_all()

# load route blueprints
app.register_blueprint(blueprint)
