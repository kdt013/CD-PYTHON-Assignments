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


if __name__ == "__main__":
    app.run(debug=True)