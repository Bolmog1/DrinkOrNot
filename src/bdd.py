import sqlite3

#connection à bdd
def db_connection():
    connect=sqlite3.connect("recette.db")
    connect.row_factory=sqlite3.Row #pour fonctionnement comme dictionnaire
    return connect

#initialisation bdd
def init_db():
    connect = db_connection()
    cursor = connect.cursor()

    #création table ingredient
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            couleur1 TEXT NOT NULL,
            couleur2 TEXT NOT NULL,
            ALCOOL REAL NOT NULL
        )
    """)
    #création table recette
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recettes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            description TEXT
        )
    """)
    #création table reliant recette et ingrédient
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recettes_ingredient (
            recette_id INTEGER NOT NULL,
            ingredient_id INTEGER NOT NULL,
            dosage INTEGER NOT NULL,
            PRIMARY KEY (recette_id, ingredient_id),
            FOREIGN KEY (recette_id) REFERENCES recettes(id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
        )
    """)

    connect.commit()
    connect.close()

def ajouter_ingredient(nom, couleur1, couleur2, alcool):
    connect=db_connection()
    cursor=connect.cursor()
    cursor.execute(
        "INSERT INTO ingredients (nom, couleur1, couleur2, alcool) VALUES (?,?,?,?)", (nom, couleur1, couleur2, alcool)
        )
    connect.commit()
    connect.close()
    
def ajouter_recette(nom: str,
                    description: str,
                    liste_ingredients: list[dict[str, int]]):
    if len(nom) > 32 or (description and len(description) > 2048):
        raise Exception("Description ou nom trop long")
    connect=db_connection()
    cursor=connect.cursor()
    cursor.execute(
        "INSERT INTO recettes(nom, description) VALUES (?, ?)",(nom, description,)
        )
    #on récupère l'id de la recette créée
    recette_id=cursor.lastrowid
    for ingredient in liste_ingredients:
        cursor.execute(
            "INSERT INTO recettes_ingredient (recette_id, ingredient_id, dosage) VALUES (?,?,?)", (recette_id, ingredient["id"], ingredient["dosage"] )
            )
    connect.commit()
    connect.close()

def recuperer_ingredients():
    connect=db_connection()
    cursor=connect.cursor()
    ingredients = cursor.execute(
        "SELECT id, nom, couleur1, couleur2, alcool FROM ingredients"
    )
    ingredients = ingredients.fetchall()
    connect.close()
    return [dict(row) for row in ingredients]

def recuperer_ingredients_recettes(recette_id: int):
    connect=db_connection()
    cursor=connect.cursor()
    ingredients = cursor.execute(
        "SELECT nom, dosage, couleur1, couleur2, ALCOOL FROM recettes_ingredient JOIN ingredients ON ingredients.id == ingredient_id WHERE recette_id = ?", (recette_id,)
    )
    ingredients = ingredients.fetchall()
    connect.close()
    return [dict(i) for i in ingredients]

def rechercher_recettes(recherche: str):
    connect=db_connection()
    cursor=connect.cursor()
    recettes_id = cursor.execute(
        "SELECT id, nom, description FROM recettes WHERE nom LIKE ? LIMIT 20", (f"{recherche}%",)
    )
    recettes = recettes_id.fetchall()
    connect.close()
    recettes = [dict(r) for r in recettes]
    for recette in recettes:
        recette["ingredient"] = recuperer_ingredients_recettes(recette["id"])
    return recettes