from src import bdd

ingredients = [
    ("Eau", "#0000ff", "#3333ff", 0.0),
    ("Grenadine", "#ff2600", "#ff6251", 0.0),
    ("Vodka", "#ffffff", "#fbf2fb", 40.0),
    ("Rhum blanc", "#f5f5f5", "#e0e0e0", 40.0),
    ("Rhum ambré", "#d2691e", "#cd853f", 40.0),
    ("Rhum brun", "#8b4513", "#a0522d", 40.0),
    ("Tequila", "#f5deb3", "#e6c229", 40.0),
    ("Whisky", "#d2691e", "#8b4513", 40.0),
    ("Gin", "#e0ffff", "#00ffff", 40.0),
    ("Absinthe", "#90ee90", "#2e8b57", 45.0),
    ("Liqueur de café", "#654321", "#4a3728", 25.0),
    ("Liqueur de menthe", "#98fb98", "#00fa9a", 25.0),
    ("Liqueur d'orange", "#ffa500", "#ff8c00", 20.0),
    ("Curaçao bleu", "#00bfff", "#1e90ff", 20.0),
    ("Curaçao orange", "#ff8c00", "#ffa500", 20.0),
    ("Triple Sec", "#ffd700", "#ffcc00", 20.0),
    ("Grand Marnier", "#ffa500", "#ff8c00", 40.0),
    ("Cointreau", "#ff8c00", "#ffa500", 40.0),
    ("Amaretto", "#d2691e", "#8b4513", 25.0),
    ("Baileys", "#f5f5dc", "#e6e6d4", 17.0),
    ("Kahlúa", "#654321", "#4a3728", 20.0),
    ("Chambord", "#8b008b", "#9932cc", 16.5),
    ("Sambuca", "#ffffff", "#f8f8ff", 40.0),
    ("Jägermeister", "#000000", "#2f2f2f", 35.0),
    ("Midori", "#00ff7f", "#2e8b57", 20.0),
    ("Pisang Ambon", "#ffd700", "#ffcc00", 22.0),
    ("Blue Curaçao", "#00bfff", "#1e90ff", 20.0),
    ("Chartreuse verte", "#90ee90", "#2e8b57", 55.0),
    ("Chartreuse jaune", "#ffff00", "#ffd700", 40.0),
    ("Pernod", "#90ee90", "#2e8b57", 40.0),
    ("Ricard", "#90ee90", "#2e8b57", 45.0),
    ("Pastis", "#90ee90", "#2e8b57", 45.0),
    ("Ouzo", "#ffffff", "#f8f8ff", 40.0),
    ("Arak", "#ffffff", "#f8f8ff", 50.0),
    ("Sake", "#f5f5f5", "#e0e0e0", 15.0),
    ("Mirin", "#ffd700", "#ffcc00", 14.0),
    ("Porto", "#8b0000", "#a52a2a", 20.0),
    ("Xérès", "#d2691e", "#8b4513", 15.0),
    ("Madère", "#8b4513", "#a0522d", 15.0),
    ("Marsala", "#8b4513", "#a0522d", 15.0),
    ("Vin rouge", "#8b0000", "#a52a2a", 12.0),
    ("Vin blanc", "#fffacd", "#fafad2", 12.0),
    ("Vin rosé", "#ffc0cb", "#ffb6c1", 12.0),
    ("Champagne", "#fffacd", "#fafad2", 12.0),
    ("Prosecco", "#fffacd", "#fafad2", 11.0),
    ("Cidre", "#ffd700", "#ffcc00", 5.0),
    ("Bière blonde", "#ffd700", "#ffcc00", 5.0),
    ("Bière brune", "#8b4513", "#a0522d", 6.0),
    ("Bière blanche", "#fffacd", "#fafad2", 5.0),
    ("Lait", "#ffffff", "#f8f8ff", 0.0),
    ("Lait de coco", "#ffffff", "#f0f8ff", 0.0),
    ("Crème liquide", "#fffacd", "#fafad2", 0.0),
    ("Jus d'orange", "#ffa500", "#ff8c00", 0.0),
    ("Jus de pomme", "#ffd700", "#ffcc00", 0.0),
    ("Jus d'ananas", "#ffd700", "#ffcc00", 0.0),
    ("Jus de cranberry", "#8b0000", "#a52a2a", 0.0),
    ("Jus de tomate", "#ff6347", "#ff4500", 0.0),
    ("Jus de citron", "#ffff00", "#ffd700", 0.0),
    ("Jus de lime", "#32cd32", "#228b22", 0.0),
    ("Jus de pamplemousse", "#ffa500", "#ff8c00", 0.0),
    ("Jus de raisin", "#800080", "#9932cc", 0.0),
    ("Jus de carotte", "#ffa500", "#ff8c00", 0.0),
    ("Jus de grenade", "#8b0000", "#a52a2a", 0.0),
    ("Sirop de sucre", "#ffffff", "#f8f8ff", 0.0),
    ("Sirop de menthe", "#98fb98", "#00fa9a", 0.0),
    ("Sirop de fraise", "#ff69b4", "#ff1493", 0.0),
    ("Sirop de framboise", "#8b008b", "#9932cc", 0.0),
    ("Sirop de cassis", "#800080", "#9932cc", 0.0),
    ("Sirop de pêche", "#ffdab9", "#ffa07a", 0.0),
    ("Sirop de vanille", "#f5f5dc", "#e6e6d4", 0.0),
    ("Sirop de caramel", "#d2691e", "#8b4513", 0.0),
    ("Sirop de chocolat", "#654321", "#4a3728", 0.0),
    ("Sirop de noisette", "#d2691e", "#8b4513", 0.0),
    ("Miel liquide", "#ffd700", "#ffcc00", 0.0),
    ("Vinaigre balsamique", "#8b4513", "#a0522d", 0.0),
    ("Vinaigre de cidre", "#ffd700", "#ffcc00", 0.0),
    ("Vinaigre de vin rouge", "#8b0000", "#a52a2a", 0.0),
    ("Huile d'olive", "#808000", "#6b8e23", 0.0),
    ("Huile de colza", "#ffd700", "#ffcc00", 0.0),
    ("Huile de noix", "#d2691e", "#8b4513", 0.0),
    ("Huile de sésame", "#ffd700", "#ffcc00", 0.0),
    ("Bouillon de volaille", "#ffd700", "#ffcc00", 0.0),
    ("Bouillon de légumes", "#90ee90", "#2e8b57", 0.0),
    ("Bouillon de bœuf", "#8b4513", "#a0522d", 0.0),
    ("Sauce soja", "#654321", "#4a3728", 0.0),
    ("Sauce Worcestershire", "#8b4513", "#a0522d", 0.0),
    ("Sauce Tabasco", "#ff4500", "#ff6347", 0.0),
    ("Sauce piquante", "#ff4500", "#ff6347", 0.0),
    ("Sauce tomate", "#ff6347", "#ff4500", 0.0),
    ("Ketchup", "#ff6347", "#ff4500", 0.0),
    ("Moutarde", "#ffd700", "#ffcc00", 0.0),
    ("Mayonnaise", "#fffacd", "#fafad2", 0.0),
    ("Crème aigre", "#fffacd", "#fafad2", 0.0),
    ("Yaourt liquide", "#ffffff", "#f8f8ff", 0.0),
    ("Lait concentré sucré", "#fffacd", "#fafad2", 0.0),
    ("Café", "#654321", "#4a3728", 0.0),
    ("Thé vert", "#90ee90", "#2e8b57", 0.0),
    ("Thé noir", "#8b4513", "#a0522d", 0.0),
    ("Infusion de fruits rouges", "#8b008b", "#9932cc", 0.0),
    ("Limonade", "#ffff00", "#ffd700", 0.0),
    ("Soda citron", "#ffff00", "#ffd700", 0.0),
    ("Soda cola", "#654321", "#4a3728", 0.0),
    ("Soda orange", "#ffa500", "#ff8c00", 0.0),
    ("Tonic", "#e0ffff", "#00ffff", 0.0),
    ("Ginger ale", "#ffd700", "#ffcc00", 0.0)
]

recettes = [
    # --- Cocktails sans alcool ---
    ("Diabolo Grenadine", "Rafraîchissant et sucré, mélange classique de grenadine et de limonade.", [
        {"id": 2, "dosage": 30},
        {"id": 103, "dosage": 180}
    ]),

    ("Diabolo Menthe", "Fraîcheur garantie avec sirop de menthe et limonade.", [
        {"id": 68, "dosage": 20},
        {"id": 103, "dosage": 180}
    ]),

    ("Jus d'Orange Pétillant", "Jus d'orange mélangé à de la limonade pour un effet pétillant.", [
        {"id": 56, "dosage": 150},
        {"id": 103, "dosage": 60}
    ]),

    ("Virgin Mojito", "Sans alcool, à base de jus de lime, sirop de sucre et soda citron.", [
        {"id": 62, "dosage": 30},
        {"id": 67, "dosage": 20},
        {"id": 104, "dosage": 150}
    ]),

    ("Sunrise Sans Alcool", "Jus d'orange et grenadine pour un effet coucher de soleil.", [
        {"id": 56, "dosage": 180},
        {"id": 2, "dosage": 20}
    ]),

    # --- Cocktails à base de vodka ---
    ("Vodka Tonic", "Classique et rafraîchissant, vodka et tonic.", [
        {"id": 3, "dosage": 40},
        {"id": 107, "dosage": 160}
    ]),

    ("Screwdriver", "Vodka et jus d'orange, simple et efficace.", [
        {"id": 3, "dosage": 40},
        {"id": 56, "dosage": 160}
    ]),

    ("Cosmopolitan", "Vodka, triple sec, jus de cranberry et jus de lime.", [
        {"id": 3, "dosage": 40},
        {"id": 19, "dosage": 15},
        {"id": 59, "dosage": 30},
        {"id": 62, "dosage": 15}
    ]),

    ("White Russian", "Vodka, liqueur de café et crème liquide pour un cocktail onctueux.", [
        {"id": 3, "dosage": 50},
        {"id": 24, "dosage": 25},
        {"id": 55, "dosage": 25}
    ]),

    ("Sea Breeze", "Vodka, jus de cranberry et jus de pamplemousse.", [
        {"id": 3, "dosage": 40},
        {"id": 59, "dosage": 90},
        {"id": 63, "dosage": 70}
    ]),

    # --- Cocktails à base de rhum ---
    ("Mojito", "Rhum blanc, jus de lime, sirop de sucre, eau gazeuse et menthe.", [
        {"id": 7, "dosage": 40},
        {"id": 62, "dosage": 20},
        {"id": 67, "dosage": 20},
        {"id": 103, "dosage": 120}
    ]),

    ("Daiquiri", "Rhum blanc, jus de lime et sirop de sucre.", [
        {"id": 7, "dosage": 50},
        {"id": 62, "dosage": 25},
        {"id": 67, "dosage": 20}
    ]),

    ("Piña Colada", "Rhum blanc, lait de coco et jus d'ananas.", [
        {"id": 7, "dosage": 50},
        {"id": 54, "dosage": 50},
        {"id": 58, "dosage": 100}
    ]),

    ("Mai Tai", "Rhum ambré, rhum blanc, liqueur d'orange, jus de lime et sirop d'amande.", [
        {"id": 8, "dosage": 30},
        {"id": 7, "dosage": 30},
        {"id": 16, "dosage": 15},
        {"id": 62, "dosage": 15},
        {"id": 22, "dosage": 10}
    ]),

    ("Zombie", "Mélange puissant de rhums, liqueurs et jus de fruits.", [
        {"id": 7, "dosage": 30},
        {"id": 9, "dosage": 30},
        {"id": 16, "dosage": 15},
        {"id": 58, "dosage": 60},
        {"id": 56, "dosage": 60},
        {"id": 59, "dosage": 15}
    ]),

    # --- Cocktails à base de gin ---
    ("Gin Tonic", "Gin et tonic, un grand classique.", [
        {"id": 12, "dosage": 40},
        {"id": 107, "dosage": 160}
    ]),

    ("Gin Fizz", "Gin, jus de citron, sirop de sucre et soda.", [
        {"id": 12, "dosage": 50},
        {"id": 61, "dosage": 20},
        {"id": 67, "dosage": 20},
        {"id": 104, "dosage": 110}
    ]),

    ("Tom Collins", "Gin, jus de citron, sirop de sucre et soda.", [
        {"id": 12, "dosage": 50},
        {"id": 61, "dosage": 30},
        {"id": 67, "dosage": 20},
        {"id": 104, "dosage": 100}
    ]),

    ("Singapore Sling", "Gin, liqueur de cerise, triple sec, jus d'ananas et jus de citron.", [
        {"id": 12, "dosage": 40},
        {"id": 2, "dosage": 10},
        {"id": 19, "dosage": 10},
        {"id": 58, "dosage": 80},
        {"id": 61, "dosage": 10}
    ]),

    # --- Cocktails à base de tequila ---
    ("Margarita", "Tequila, triple sec et jus de lime.", [
        {"id": 10, "dosage": 50},
        {"id": 19, "dosage": 20},
        {"id": 62, "dosage": 20}
    ]),

    ("Sunrise", "Tequila, jus d'orange et grenadine.", [
        {"id": 10, "dosage": 40},
        {"id": 56, "dosage": 150},
        {"id": 2, "dosage": 10}
    ]),

    ("Paloma", "Tequila, jus de pamplemousse et soda.", [
        {"id": 10, "dosage": 50},
        {"id": 63, "dosage": 100},
        {"id": 104, "dosage": 50}
    ]),

    # --- Cocktails à base de whisky ---
    ("Whisky Sour", "Whisky, jus de citron, sirop de sucre et blanc d'œuf (remplacé ici par sirop de sucre).", [
        {"id": 11, "dosage": 50},
        {"id": 61, "dosage": 25},
        {"id": 67, "dosage": 20}
    ]),

    ("Manhattan", "Whisky, vermouth rouge (remplacé par vin rouge) et angostura (remplacé par sirop de sucre).", [
        {"id": 11, "dosage": 60},
        {"id": 44, "dosage": 30},
        {"id": 67, "dosage": 10}
    ]),

    ("Rusty Nail", "Whisky et liqueur de café.", [
        {"id": 11, "dosage": 50},
        {"id": 24, "dosage": 25}
    ]),

    # --- Cocktails à base de liqueurs ---
    ("B-52", "Café, Baileys et Grand Marnier en couches.", [
        {"id": 99, "dosage": 30},
        {"id": 23, "dosage": 30},
        {"id": 20, "dosage": 30}
    ]),

    ("Amaretto Sour", "Amaretto, jus de citron et sirop de sucre.", [
        {"id": 22, "dosage": 40},
        {"id": 61, "dosage": 30},
        {"id": 67, "dosage": 20}
    ]),

    ("Midori Sour", "Midori, jus de citron et soda citron.", [
        {"id": 28, "dosage": 40},
        {"id": 61, "dosage": 20},
        {"id": 104, "dosage": 140}
    ]),

    # --- Cocktails à base de champagne ---
    ("Bellini", "Champagne et purée de pêche (remplacée par jus de pêche).", [
        {"id": 47, "dosage": 120},
        {"id": 72, "dosage": 30},
        {"id": 1, "dosage": 50}
    ]),

    ("Mimosa", "Champagne et jus d'orange.", [
        {"id": 47, "dosage": 100},
        {"id": 56, "dosage": 100}
    ]),

    ("French 75", "Gin, champagne, jus de citron et sirop de sucre.", [
        {"id": 12, "dosage": 30},
        {"id": 47, "dosage": 120},
        {"id": 61, "dosage": 15},
        {"id": 67, "dosage": 10}
    ]),

    # --- Cocktails exotiques ---
    ("Blue Lagoon", "Vodka, blue curaçao, jus de citron et soda.", [
        {"id": 3, "dosage": 40},
        {"id": 30, "dosage": 20},
        {"id": 61, "dosage": 20},
        {"id": 104, "dosage": 120}
    ]),

    ("Green Fairy", "Absinthe, sirop de sucre et eau.", [
        {"id": 13, "dosage": 30},
        {"id": 67, "dosage": 20},
        {"id": 1, "dosage": 150}
    ]),

    ("Harvey Wallbanger", "Vodka, jus d'orange et Galliano (remplacé par liqueur de vanille).", [
        {"id": 3, "dosage": 40},
        {"id": 56, "dosage": 120},
        {"id": 73, "dosage": 10}
    ]),

    # --- Cocktails chauds ---
    ("Irish Coffee", "Whisky, café, sirop de sucre et crème liquide.", [
        {"id": 11, "dosage": 40},
        {"id": 99, "dosage": 120},
        {"id": 67, "dosage": 10},
        {"id": 55, "dosage": 30}
    ]),

    ("Hot Buttered Rum", "Rhum brun, beurre (remplacé par crème liquide), sirop de sucre et eau chaude.", [
        {"id": 9, "dosage": 50},
        {"id": 55, "dosage": 20},
        {"id": 67, "dosage": 20},
        {"id": 1, "dosage": 110}
    ])
]

def ajout_ingredient():
    for ingredient in ingredients:
        bdd.ajouter_ingredient(ingredient[0], ingredient[1], ingredient[2], ingredient[3])

def ajout_recette():
    for recette in recettes:
        bdd.ajouter_recette(recette[0], recette[1], recette[2], 1, 0)