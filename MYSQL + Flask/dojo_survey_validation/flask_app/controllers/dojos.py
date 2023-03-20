from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/submit", methods=["post"])
def submit():

    if not Dojo.validate_user(request.form):
        return redirect("/")
    Dojo.save(request.form)

    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]

    return redirect("/completed_form")

@app.route("/completed_form")
def complete():
    return render_template("submit.html")

@app.route("/home")
def home():
    return redirect("/")