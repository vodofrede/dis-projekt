# DIS Projekt

## Installing / compiling

Requires an installation and PATH-available version of Python 3+.

Copy `.env.example` to `.env` and edit the file, assigning required variables (such as DB URI).

To install requirements and run the app:  
**Windows**: `.\start.bat`.  
**Unix**: `./start.sh` (requires bash).

This will make a `.venv` folder and run the app inside it.

## Database

The project was developed using a PostgreSQL database, and is not tested on e.g. MySQL or SQLite.
If using default settings, create a new database using `psql` called `dis` with the username and password `postgres`, running on `localhost:5432`.

`psql -U postgres -c "CREATE DATABASE dis OWNER postgres`

The `dataset/recipes.csv` file can be imported to provide some example recipes.

## Interactivity

The web app is presented as a list of recipes. In the top bar, the user can choose to register and login for the web app.
Once the user is signed up, they can add a new recipe, and will be taken to a new site where a form is presented.
Logged in users can also delete existing recipes, but only the recipes they themselves have created. If a user tries to create
or delete recipes without being logged in, they will recieve an unauthorization error.
The user can click on the title of a recipe to view it by itself in full view.
The user can always return to the front page by clicking the giant ReciPy logo in the top bar.
Recipes keep track of the date of creation and who made it, for extra security - so that random users cannot delete eachothers recipes.
