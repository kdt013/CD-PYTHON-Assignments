from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print("you're accessing the index route!")
    return "Hello World!"

@app.route("/dojo")
def second():
    print("you're accessing the second route!")
    return "Dojo"

@app.route("/say/<name>")
def say_name(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:times>/<word>")
def repeat_times(word, times):
    repeated = word * times
    return repeated

if __name__ == "__main__":
    app.run(debug = True)