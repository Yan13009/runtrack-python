# Initialisation du produit
produit = {
    'nom': 'Ordinateur portable',
    'prix_unitaire': 1000.0,
    'quantite_stock': 50
}

# Affichage des informations initiales
print("Informations initiales du produit :")
print(f"Nom: {produit['nom']}")
print(f"Prix unitaire: {produit['prix_unitaire']} euros")
print(f"Quantité en stock: {produit['quantite_stock']} unités\n")

# Ajout de produits en stock
quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter en stock : "))
produit['quantite_stock'] += quantite_ajoutee

# Mise à jour du prix après inflation
produit['prix_unitaire'] *= 1.10  # Augmentation de 10%

# Affichage des informations mises à jour
print("\nInformations mises à jour du produit :")
print(f"Nom: {produit['nom']}")
print(f"Prix unitaire après inflation: {produit['prix_unitaire']} euros")
print(f"Quantité en stock: {produit['quantite_stock']} unités")
