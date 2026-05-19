from flask import request, flash
from src.bdd import *

def request_add_ingredient() -> None:
    nom = request.form.get("name")
    main_color = request.form.get("main_color")
    secondary_color = request.form.get("secondary_color")
    alcool = request.form.get("alcool")
    try:
        ajouter_ingredient(nom, main_color, secondary_color, alcool)
    except Exception as e:
        flash(f"Erreur ajout de l'ingrédient: {e}", "danger")
        return
    flash(f"{nom} ajouté !")  # Confirme à l'utilisateur

def request_add_recette() -> None:
    print(request.form)
    nom = request.form.get("name")
    desc = request.form.get("description")
    nb_persons = request.form.get("nb_persons", 1, int)
    original_id = request.form.get("remix", 0, int)
    ingredients_id = request.form.getlist("ingredient_id[]", int)
    ingredients_amount = request.form.getlist("amount_ml[]", float)
    print(ingredients_id, ingredients_amount)
    ingredients = [
        {
            "id": ingredients_id[i],
            "dosage": ingredients_amount[i]
        }
        for i in range(0, len(ingredients_id))
    ]
    try:
        ajouter_recette(nom, desc, ingredients,nb_persons, original_id)
    except Exception as e:
        flash(f"Erreur ajout de la recette: {e}", "danger")
        return
    flash(f"{nom} ajouté !")
