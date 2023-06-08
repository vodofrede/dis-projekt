import datetime
import os

import flask_login
import psycopg2

# initialize models
con = psycopg2.connect(os.environ["APP_DB_URI"])

# initialize tables
with open("schema/create.sql") as sql:
    cur = con.cursor()

    cur.execute(sql.read())

    con.commit()
    cur.close()


class Recipe:
    id: int
    name: str
    category: str
    cuisine: str
    ingredients: str
    description: str
    method: str
    created_by: int
    created_by_username: str
    created_at: datetime.datetime

    def __init__(self, recipe):
        self.rid = recipe[0]
        self.name = recipe[1]
        self.category = recipe[2]
        self.cuisine = recipe[3]
        self.ingredients = recipe[4]
        self.description = recipe[5]
        self.method = recipe[6]
        self.created_by = recipe[7]
        self.created_at = recipe[8]

        user = User.by_user_id(self.created_by)
        if user is not None:
            self.created_by_username = user.id
        else:
            self.created_by_username = "System"

    def ingredient_list(self):
        return self.ingredients.split(";")

    def method_list(self):
        return self.method.split(";")

    def pretty_date(self):
        return self.created_at.strftime("%d/%m-%Y")

    @staticmethod
    def get_all_recipes():
        cur = con.cursor()
        sql = """
        SELECT * FROM Recipes order by rid desc;
        """
        cur.execute(sql)
        recipe_data = cur.fetchall()
        recipes = [Recipe(data) for data in recipe_data]

        cur.close()

        return recipes

    # get 'n' recipes in database

    @staticmethod
    def get_recipes(amount, fromId):
        cur = con.cursor()
        sql = """
        SELECT * FROM Recipes where rid > %s order by rid limit %s
        """

        cur.execute(sql, (fromId, amount))
        recipes = cur.fetchall()
        cur.close()
        return recipes

    # get recipe by id

    @staticmethod
    def getRecipeById(id):
        cur = con.cursor()

        sql = """
        SELECT * FROM Recipes where rid = %s
        """

        cur.execute(sql, (id,))

        recipe = Recipe(cur.fetchone()) if cur.rowcount > 0 else None
        cur.close()
        return recipe

    # get recipe by id

    def deleteRecipe(id):
        cur = con.cursor()

        sql = """
        DELETE FROM Recipes where rid = %s
        """

        cur.execute(sql, (id,))

        con.commit()
        cur.close()

    # get recipe by id

    @staticmethod
    def addRecipe(recipe):
        cur = con.cursor()
        sql = """
        INSERT INTO Recipes(name, category, cuisine, ingredients, description, method, 
        created_by) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cur.execute(
            sql,
            (
                recipe[0],
                recipe[1],
                recipe[2],
                recipe[3],
                recipe[4],
                recipe[5],
                recipe[6],
            ),
        )

        con.commit()
        cur.close()


class User(flask_login.UserMixin):
    id: str
    user_id: int
    password: str

    @staticmethod
    def get_user(id):
        """
        Checks if a id is in the database and
        returns the user if it is the case, otherwise it returns None
        if the user does not exist.
        """

        cur = con.cursor()
        sql = """
        SELECT * FROM Users WHERE username = %s
        """

        cur.execute(sql, (id,))

        # check if query returned unique result
        user_data = cur.fetchone() if cur.rowcount > 0 else None
        if user_data is None:
            return None

        user = User()
        user.user_id = user_data[0]
        user.id = user_data[1]
        user.password = user_data[2]

        cur.close()
        return user

    @staticmethod
    def by_user_id(user_id):
        """
        Checks if a id is in the database and
        returns the user if it is the case, otherwise it returns None
        if the user does not exist.
        """

        cur = con.cursor()
        sql = """
        SELECT * FROM Users WHERE id = %s
        """

        cur.execute(sql, (user_id,))

        # check if query returned unique result
        user_data = cur.fetchone() if cur.rowcount > 0 else None
        if user_data is None:
            return None

        user = User()
        user.id = user_data[1]
        user.password = user_data[2]

        cur.close()
        return user

    @staticmethod
    def register_user(id, password):
        """
        Register a new user. Don't do any checks, as we assume that this method won't
        be called with an existing username. Always returns a user.
        """

        cur = con.cursor()
        sql = """
        INSERT INTO Users(username, password) VALUES (%s, %s)
        """

        cur.execute(
            sql,
            (
                id,
                password,
            ),
        )

        con.commit()
        cur.close()

        user = User()
        user.id = id
        user.password = password

        return user
