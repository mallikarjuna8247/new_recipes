import os
import app
from flask import Flask, render_template, request, redirect, url_for, session,flash
import sqlite3
import bcrypt
import hashlib

conn = sqlite3.connect('myrecipes.db')
cursor = conn.cursor()


def connect_db():
    conn = sqlite3.connect('myrecipes.db')
    return conn


# table_name = "customers"
# sql_create_table = f'''
#     CREATE TABLE if not exists {table_name} (
#         user_id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     )'''
#
# conn.execute(sql_create_table)

app = Flask(__name__)
app.secret_key = os.urandom((24))

def save_user(username, password,email,Age):
    conn = connect_db()
    cursor = conn.cursor()

    # Validate data (optional)
    if not username or not password or not email or not Age:
        return "Please enter a username and password."

    # Hash password before storing (highly recommended)
    # Use a secure hashing algorithm like bcrypt
    hashed_password =  bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor.execute("INSERT INTO users (username, password,email,Age) VALUES (?, ?,?,?)",
                   (username, hashed_password,email,Age))
    conn.commit()
    conn.close()
    return "User registered successfully!"

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    Age = request.form["Age"]

    if username and password and email and Age:
      save_user(username, password,email,Age)
      return "Registration successful!"
    else:
      return "Please enter a username and password."
  else:
    return render_template("register.html")

@app.route("/Home", methods=["GET", "POST"])
def Home():

    return render_template("Home.html")

#
# table_name = "recipes"
# sql_recipe_table = f'''
#     CREATE TABLE if not exists {table_name} (
#         ID INTEGER PRIMARY KEY,
#         Title String NOT NULL,
#         Description TEXT,
#         Ingredients TEXT,
#         Instructions TEXT,
#         Created_by TEXT
#     )'''
#
# conn.execute(sql_recipe_table)

def get_recipes():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    conn.close()

    return recipes


def check_password_match(provided_password, stored_hashed_password):
    try:
        # Decode the stored hashed password
        stored_hashed_password = stored_hashed_password.encode("utf-8")

        # Check if the provided password matches the stored hashed password
        return bcrypt.checkpw(provided_password.encode("utf-8"), stored_hashed_password)
    except Exception as e:
        return str(e)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify password hash
def verify_password(input_password, stored_password):
    return input_password == stored_password


def get_items(page=1, per_page=10):
    # Calculate the offset
    offset = (page - 1) * per_page

    # Query the database
    conn = sqlite3.connect('myrecipes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes LIMIT ? OFFSET ?", (per_page, offset))
    recipes = cursor.fetchall()

    # Close the connection
    conn.close()

    return recipes

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('myrecipes.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()


        if user:
            stored_password = user[4]
            session['username'] = username
            if verify_password(hash_password(password), stored_password):
                flash('Login successful!', 'success')
                recipes = get_recipes()
                return render_template("dashboard.html", recipes=recipes)
        else:
            error = 'Invalid username or password'
            return render_template('index.html', error=error)
        conn.close()
    page = request.args.get('page', 1, type=int)
    per_page = 10
    has_next = len(get_items()) == per_page

    # Fetch items for the current page
    items = get_items(page, per_page)

    return render_template("dashboard.html", recipes=items,page=page,per_page=has_next)

def add_recipe(Title, Description,Ingredients,Instructions,Created_by):

    conn = connect_db()
    cursor = conn.cursor()

    # Validate data (optional)
    if not Title or not Description or not Ingredients or not Instructions or not Created_by:
        return "Please enter a recipe name and description."

    cursor.execute(f"INSERT INTO recipes (Title, description,Ingredients,Instructions,Created_by) VALUES (?,?,?,?,?)",(Title,Description,Ingredients,Instructions,Created_by))
    conn.commit()
    conn.close()
    return "Recipe added successfully!"

@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    if request.method == "POST":
        Title = request.form["Title"]
        Description = request.form["Description"]
        Ingredients = request.form["Ingredients"]
        Instructions = request.form["Instructions"]
        Created_by =  session.get('username')

        try:
            message = add_recipe(Title, Description, Ingredients, Instructions,Created_by)
            page = request.args.get('page', 1, type=int)
            per_page = 10
            has_next = len(get_items()) == per_page

            # Fetch items for the current page
            items = get_items(page, per_page)

            return render_template("dashboard.html", recipes=items,page=page,per_page=has_next)  # Display success message or handle errors
        except sqlite3.Error as e:
            return f"Error adding recipe: {e}"

    return render_template("Addrecipe.html")

def get_recipe(recipe_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    recipe = cursor.fetchone()
    conn.close()

    return recipe

# Function to update a recipe
def update_recipe(Title, Description, Ingredients,Instructions,ID):

    conn = connect_db()
    cursor = conn.cursor()

    # Validate data (optional)
    if not Title or not Description or not Ingredients or not Instructions or not ID:
        return "Please enter a Title,description,Ingredients,Instructions,ID."

    cursor.execute("UPDATE recipes SET Title = ?, description = ?,Ingredients=?,Instructions=? WHERE ID = ?",
                   (Title, Description, Ingredients,Instructions,ID))
    conn.commit()
    conn.close()
    page = request.args.get('page', 1, type=int)
    per_page = 10
    has_next = len(get_items()) == per_page

    # Fetch items for the current page
    items = get_items(page, per_page)
    return render_template("dashboard.html", recipes=items,page=page,per_page=has_next)



@app.route("/recipes/<int:ID>")
def view_recipes(ID):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    conn.close()
    page = request.args.get('page', 1, type=int)
    per_page = 10
    has_next = len(get_items()) == per_page

    # Fetch items for the current page
    items = get_items(page, per_page)
    return render_template('dashboard.html', recipes=items,page=page,per_page=has_next)

@app.route("/edit_recipe/<int:ID>", methods=["GET", "POST"])
def edit_recipe(ID):
    if request.method == "GET":
        recipe = get_recipe(ID)
        if not recipe:
            return "Recipe not found!"

        return render_template("Editrecipe.html", recipe=recipe)

    if request.method == "POST":
        Title = request.form["Title"]
        description = request.form["Description"]
        Ingredients = request.form["Ingredients"]
        Instructions = request.form["Instructions"]
        #ID = request.form["ID"]
        ID = int(ID)

        try:
            message = update_recipe( Title, description,Ingredients,Instructions,ID)
            page = request.args.get('page', 1, type=int)
            per_page = 10
            has_next = len(get_items()) == per_page

            # Fetch items for the current page
            items = get_items(page, per_page)
            return render_template('dashboard.html', recipes=items, page=page, per_page=has_next)

        except sqlite3.Error as e:
            return f"Error updating recipe: {e}"

def delete_recipe_handler(ID):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM recipes WHERE id = ?", (ID,))
    conn.commit()
    conn.close()
    return "Recipe deleted successfully!"
    #return render_template("recipes.html", recipes=recipes)

@app.route("/delete_recipe/<int:ID>", methods=["GET", "POST"])
def delete_recipe(ID):
    if request.method == "GET":
        recipe = get_recipe(ID)
        return render_template("Deleterecipe.html", recipe=recipe, recipe_id=ID)

    if request.method == "POST":
        try:
            message = delete_recipe_handler(ID)
            page = request.args.get('page', 1, type=int)
            per_page = 10
            has_next = len(get_items()) == per_page

            # Fetch items for the current page
            items = get_items(page, per_page)
            return render_template('dashboard.html', recipes=items, page=page, per_page=has_next)
        except sqlite3.Error as e:
            return f"Error deleting recipe: {e}"  # Handle database errors

# Optional function to retrieve a recipe by ID (for confirmation display)
def get_recipe(recipe_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    recipe = cursor.fetchone()
    conn.close()

    return recipe

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        conn = connect_db()
        cursor = conn.cursor()
        search_query = request.form.get('search_query')
        query = """
                SELECT * FROM recipes 
                WHERE Title LIKE ? OR Ingredients LIKE ?
                """
        # Execute the search query (modify as needed)
        cursor.execute("""
                SELECT * FROM recipes 
                WHERE Title LIKE ? OR Ingredients LIKE ?
                """,('%' + str(search_query) + '%', '%' + str(search_query) + '%',))
        results = cursor.fetchall()
        return render_template('search_results.html', recipes=results)
    return render_template('search_form.html')

@app.route('/logout')
def logout():
    # Remove user session data
    session.pop('username', None)  # Remove 'username' or any other session variable
    # Optionally, flash a message
    flash('You have been logged out!', 'success')
    return redirect(url_for('Home'))  # Redirect to main page after logout


if __name__ == "__main__":
  app.run(debug=True)
