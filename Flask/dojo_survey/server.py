from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "form"

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/submit", methods=["post"])
def submit():
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

if __name__ == "__main__":
    app.run(debug = True)