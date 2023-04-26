import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

# database models


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
