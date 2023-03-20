from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", users=users)

@app.route("/submit", methods=["post"])
def form():
    print(request.form)
    data = {
        "first_name": request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    User.save(data)
    return redirect("/")

@app.route("/create")
def create_form():
    return render_template("create.html")

@app.route("/show/<int:id>")
def display_user(id):
    data = {
        "id":id
    }
    return render_template("show_user.html", users=User.show(data))

@app.route("/show/<int:id>/edit")
def edit_user(id):
    data = {
        "id":id
    }
    single_user = User.show(data)
    return render_template("edit.html", single_user=single_user)

@app.route("/update/<int:id>", methods=["post"])
def update_user(id):
    data = {
    "id":id,
    "first_name": request.form["first_name"],
    "last_name":request.form["last_name"],
    "email":request.form["email"]
    }
    User.update(data)
    return redirect('/')

@app.route("/delete/<int:id>")
def delete_user(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)