from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("login_page.html")

@app.route("/register", methods=["post"])
def register_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"],
    }
    this_user = User.find_one_by_email(data)

    if this_user:
        flash("Email is already in use!")
        return redirect("/")


    if not User.validate(data):
        print("not valid")
        return redirect("/")
    
    #information IS valid

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data["password"] = pw_hash
    # print(f"password: {request.form['password']}")
    # print(f"hashed password: {pw_hash}")

    user_id = User.save(data)
    session["logged_id"] = user_id

    return redirect("/main")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/success")
def success():
    if "logged_id" not in session:
        return redirect("/")

    data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(data)

    return render_template("dashboard.html", logged_user=logged_user)


@app.route("/login", methods=["post"])
def login_user():
    data = {
        "email": request.form["email"]
    }

    this_user = User.find_one_by_email(data)
    if not this_user:
        flash("Invalid email or password")
        return redirect("/")
    # check if the user by that id already exists
    # if they don't,   
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("password is wrong")
        return redirect("/")

    session["logged_id"] = this_user.id
    # if it does exist
        #check the password, compare hashed passwords to see if they are equal
        # if they are equal, you logged in!
        # if not equal, then flash message and redirect to form page
    print("successful login")
    return redirect("/main")