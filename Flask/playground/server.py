from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print("you're accessing the index route!")
    return "Hello World!"

@app.route("/play")
def main():
    return render_template("index.html")

@app.route("/play/<int:times>")
def play(times):
    return render_template("index.html",times=times)

@app.route("/play/<color>/<int:times>")
def color(color,times):
    return render_template("index.html",color=color,times=times)

if __name__ == "__main__":
    app.run(debug = True)
