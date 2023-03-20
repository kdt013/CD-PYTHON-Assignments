from flask import Flask, render_template, redirect, request
app = Flask(__name__)
from flask_app.models.sundaes import Sundae

@app.route("/")
def index():
    all_sundaes = Sundae.get_all()
    print(all_sundaes)
    return render_template("index.html")

@app.route("/sundaes/new")
def create_form():
    return render_template("create_form.html")


if __name__ == "__main__":
    app.run(debug=True)