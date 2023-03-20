from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def dojos():
    dojo_name = Dojo.get_all()
    print(dojo_name)
    return render_template("dojos.html", dojo_name=dojo_name)

@app.route("/dojos", methods=["POST"])
def new_dojo():
    print(request.form)
    data = {
        "name": request.form["name"]
    }
    dojo_id=Dojo.save(data)
    print(dojo_id)
    return redirect("/")

@app.route("/ninjas")
def new_ninja():
    dojo_name = Dojo.get_all()
    print(dojo_name)
    return render_template("new_ninja.html", dojo_name=dojo_name)

@app.route("/create_new", methods=["POST"])
def list_ninjas():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["location"],
    }
    Ninja.save(data)
    return redirect("/")

@app.route("/dojo_show/<int:id>")
def show_ninjas(id):
    print(id)
    data = {
        "id": id
    }
    print(data)
    dojo_ninjas = Dojo.ninjas_in_dojo(data)
    print(dojo_ninjas.ninjas)
    return render_template("dojo_show.html", dojo_ninjas=dojo_ninjas)
