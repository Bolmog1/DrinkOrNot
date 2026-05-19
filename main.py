from flask import Flask, request, render_template, url_for, redirect
from src.controller import *
from src.bdd import *

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

init_db()

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
        remix = request.args.get('remix', None, int)
        recette = None
        if remix:
            recette = dict(recuperer_recettes(remix)[0])
            recette["ingredients"] = recuperer_ingredients_recettes(remix)
        return render_template("recette.html", ingredients=ingredients, recette=recette)
    elif request.method == 'POST':
        request_add_recette()
        return redirect(url_for("recette"))
    return None

@app.route("/recherche", methods=["GET"])
def recherche():
    query = request.args.get('q', '')
    avec_alcool=request.args.get("alcool")=="on"
    recettes = rechercher_recettes(query, avec_alcool)
    print(recettes)
    return render_template("recherche.html", recettes=recettes, query=query)

@app.route("/recette/<id>", methods=["GET"])
def recette_by_id(id: int):
    recette = recuperer_recettes(id)[0]
    ingredients = recuperer_ingredients_recettes(id)
    return render_template("preview.html", recette=recette, ingredients=ingredients)
