from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tv_show import TV_Show
# from flask_app.models.recipe import Recipe

@app.route("/main")
def main_page():
    if "logged_id" not in session:
            return redirect("/")

    data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(data)

    # pull data for all tv_shows
    all_tv_shows = TV_Show.get_all_tv_shows()
    for item in all_tv_shows:
        print(item.title)
    return render_template("dashboard.html", logged_user=logged_user, all_tv_shows=all_tv_shows)


@app.route("/tv_show/new")
def add_new_show():
    if "logged_id" not in session:
            return redirect("/")
    return render_template("new_show.html")


@app.route("/tv_show/submit", methods=["POST"])
def submit_new_show():
    if "logged_id" not in session:
            return redirect("/")
    
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "users_id": session["logged_id"]
    }
    if not TV_Show.validate(data):
        return redirect("/tv_show/new")

    TV_Show.save(data)

    return redirect("/main")

@app.route("/tv_shows/<int:id>/view")
def view_show(id):
    if "logged_id" not in session:
            return redirect("/")
    
    data = {
        "id": id
        }
    one_show = TV_Show.get_one(data)

    data_creator = {
        "id": one_show.users_id
    }
    show_poster = User.find_one_by_id(data_creator)

    return render_template("view_show.html", one_show=one_show, show_poster=show_poster)

@app.route("/tv_shows/<int:id>/edit")
def edit_tv_show(id):
    if "logged_id" not in session:
            return redirect("/")

    data = {
        "id": id
    }

    one_tv_show = TV_Show.get_one(data)

    return render_template("edit.html", one_tv_show=one_tv_show)

@app.route("/tv_show/submit/edit", methods=["POST"])
def submit_edit():
    print(request.form)
    id = request.form["id"]
    
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "users_id": session["logged_id"]
    }

    if not TV_Show.validate(data):
        return redirect("/tv_shows/" + str(id) + "/edit")

    TV_Show.edit_show(data)

    return redirect("/main")

@app.route("/tv_shows/<int:id>/delete")
def delete_tv_show(id):
    if "logged_id" not in session:
            return redirect("/")
    
    data = {
        "id": id
    }

    TV_Show.delete_show(data)

    return redirect("/main")