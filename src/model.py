import psycopg2

# database models

con = psycopg2.connect("dbname=dis user=postgres")

class Model():
    def __init__(self):
        pass

class Recipe(Model):
    # recipe: 
    # id, name, category, views, votes, cuisine, **ingredients**, time, difficulty

    def __init__(self):
        super.__init__()    

    # get 'n' recipes by category
    @staticmethod
    def by_category(amount):
        pass

    # get 'n' recipes in database
    @staticmethod
    def n_recipes(amount):
        pass

class Ingredient(Model):
    # ingredient: id, name, category
    pass

class User(Model):
    # user: id, user_name, favorite_recipes
    pass
