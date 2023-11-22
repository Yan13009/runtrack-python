def verifier_pair_impair(nombre):
   
    if isinstance(nombre, int) and nombre >= 0:
       
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")


nombre_utilisateur = int(input("Entrez un nombre entier positif : "))
verifier_pair_impair(nombre_utilisateur)
