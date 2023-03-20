from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.email import Email

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/submit", methods=["post"])
def submit():
    if not Email.validate_email(request.form):
        return redirect('/')
    print(request.form)
    data = {
        "email":request.form["email"]
    }
    Email.save(request.form)
    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html", email=Email.get_all())
