from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "count"

@app.route("/")
def page():
    if "counter" not in session:
        session["counter"] = 1
    # else:
    #     session["counter"] += 1
    return render_template("index.html")


@app.route("/visits")
def count():
    session["counter"] += 1
    return redirect("/")


@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


# use session to increment the button
# use session to reset