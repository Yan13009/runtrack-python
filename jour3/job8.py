def afficher_produits(type_produit, saison):
    fruits_hiver = "Orange, mandarine et kiwi"
    fruits_ete = "Poire, fraise, cassis"
    legumes_hiver = "Carotte, topinambour, endive"
    legumes_ete = "Artichaut, aubergine, navet"

    if type_produit == "fruits" and saison == "hiver":
        print(fruits_hiver)
    elif type_produit == "fruits" and saison == "ete":
        print(fruits_ete)
    elif type_produit == "legume" and saison == "hiver":
        print(legumes_hiver)
    elif type_produit == "legume" and saison == "ete":
        print(legumes_ete)
    else:
        print("Combinaison type/season non reconnue.")

if __name__ == "__main__":
    import sys

    # Vérifiez si des arguments de ligne de commande ont été fournis
    if len(sys.argv) == 3:
        type_produit = sys.argv[1]
        saison = sys.argv[2]
        afficher_produits(type_produit, saison)
    else:
        print("Veuillez fournir le type et la saison en arguments de la ligne de commande.")
