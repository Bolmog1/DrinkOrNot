from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ingredient", methods=["GET", "POST"])
def ingredient():
    if request.method == 'GET':
        return render_template("ingredient.html")
    elif request.method == 'POST':
        return "Not implemented yet"