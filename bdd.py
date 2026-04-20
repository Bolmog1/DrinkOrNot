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
            nom TEXT NOT NULL
        )
    """)
    #création table reliant recette et ingrédient
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recettes_ingredient (
            recette_id INTEGER NOT NULL,
            ingredient_id INTEGER NOT NULL,
            PRIMARY KEY (recette_id, ingredient_id),
            FOREIGN KEY (recette_id) REFERENCES recettes(id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredient(id)
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
    
def ajouter_recette(nom, liste_ingredients):
    connect=db_connection()
    cursor=connect.cursor()
    cursor.execute(
        "INSERT INTO recettes(nom) VALUES (?)",(nom,)
        )
    #on récupère l'id de la recette créé
    recette_id=cursor.lastrowid
    for ingredient_id in liste_ingredients:
        cursor.execute(
            "INSERT INTO recettes_ingredient (recette_id, ingredient_id) VALUES (?,?)", (recette_id, ingredient_id)
            )
    connect.commit()
    connect.close()