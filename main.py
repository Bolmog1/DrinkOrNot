from flask import Flask, request, render_template, url_for, redirect
from src.controller import *
from src.bdd import *

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ingredient", methods=["GET", "POST"])
def ingredient():
    if request.method == 'GET':
        return render_template("ingredient.html")
    elif request.method == 'POST':
        request_add_ingredient()
        return redirect(url_for("ingredient"))
    return None

@app.route("/recette", methods=["GET", "POST"])
def recette():
    if request.method == 'GET':
        ingredients = recuperer_ingredients()
        return render_template("recette.html", ingredients=ingredients)
    elif request.method == 'POST':
        request_add_recette()
        return redirect(url_for("recette"))
    return None
