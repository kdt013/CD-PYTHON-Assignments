from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route("/main")
def main_page():
    if "logged_id" not in session:
            return redirect("/")

    data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(data)

    # pull data for all recipes
    all_recipes = Recipe.get_all_recipes()
    return render_template("dashboard.html", logged_user=logged_user, all_recipes=all_recipes)

@app.route("/recipes/new")
def create_recipe_page():
    if "logged_id" not in session:
            return redirect("/")
    return render_template("new_recipe.html")

@app.route("/recipes/submit", methods=["POST"])
def submit_recipe():
    if "logged_id" not in session:
            return redirect("/")
    print("trying to submit recipe!")

    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date": request.form["date"],
        "time": request.form["time"],
        "users_id": session["logged_id"]  
    }

    if not Recipe.validate(data):
        return redirect("/recipes/new")

    Recipe.save(data)

    return redirect("/main")

@app.route("/recipes/<int:id>/edit")
def edit_recipe_page(id):
    data = {
        "id": id
    }

    one_recipe = Recipe.get_one(data)

    return render_template("edit_recipe.html", one_recipe=one_recipe)

@app.route("/recipes/submit/edit", methods=["POST"])
def submit_edit_recipe():
    print(request.form)

    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date": request.form["date"],
        "time": request.form["time"],
        "id": request.form["id"] 
    }

    Recipe.edit_recipe(data)

    return redirect("/main")

@app.route("/recipes/<int:id>/view")
def view_recipe(id):
    if "logged_id" not in session:
        return redirect("/")

    data = {
        "id": session['logged_id']
        }
    logged_user = User.find_one_by_id(data)

    data = {
        "id": id
        }
    one_recipe = Recipe.get_one(data)

    data_user = {
        "id": id
        }
    recipe_creator = User.find_one_by_id(data_user)

    return render_template("view_recipe.html", one_recipe=one_recipe, logged_user=logged_user, recipe_creator=recipe_creator)

@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    if "logged_id" not in session:
        return redirect("/")
    
    data = {
        "id": id
    }

    Recipe.delete_recipe(data)

    return redirect("/main")

