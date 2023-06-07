import psycopg2

# database models

con = psycopg2.connect("dbname=dis user=postgres")

class Model():
    def __init__(self):
        pass

class Recipe(Model):
    # recipe: 
    # id, name, category, cuisine, **ingredients**, time, difficulty

    def __init__(self, recipe):
        self.id = recipe[0]
        self.name = recipe[1]
        self.category = recipe[2]
        self.cuisine = recipe[3]
        self.ingredients = recipe[4]

        super.__init__()    

    # get all recipes
    @staticmethod
    def selectAllRecipes():
        cur = con.cursor()
        sql = """
        SELECT * FROM Recipe
        """
        cur.execute(sql)
        con.commit()
        cur.close()

    # get 'n' recipes in database
    @staticmethod
    def selectNRecipes(amount, fromId):
        cur = con.cursor()
        sql = """
        SELECT * FROM Recipe where id > %s order by id limit %s
        """
        cur.execute(sql, (fromId, amount))
        con.commit()
        cur.close()

    # get recipe by id
    @staticmethod
    def getRecipeById(id):
        cur = con.cursor()
        sql = """
        SELECT * FROM Recipe where id = %s
        """
        cur.execute(sql, (id))
        con.commit()
        cur.close()

    # get recipe by id
    @staticmethod
    def addRecipe(name, category, cuisine, ingredients):
        cur = con.cursor()
        sql = """
        INSERT INTO Recipe(name, category, cuisine, ingredients) VALUES (%s, %s, %s, %s)
        """
        cur.execute(sql, (name, category, cuisine, ingredients))
        con.commit()
        cur.close()

class Ingredient(Model):
    # ingredient: id, name, category
    def __init__(self, ingredient):
        self.id = ingredient[0]
        self.name = ingredient[1]
        self.category = ingredient[2]

class User(Model):
    # user: id, user_name, favorite_recipes, password
    def __init__(self, user):
        self.id = user[0]
        self.user_name = user[1]
        self.favorite_recipes = user[2]
        self.password = user[3]
