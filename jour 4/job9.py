def recuperer_info_liste(liste):
    
    if not liste:
        print("La liste est vide.")
        return None

    
    valeur = liste[0]
    maximum = max(liste)
    minimum = min(liste)

    return valeur, maximum, minimum


L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]


resultat = recuperer_info_liste(L)


print("Valeur de la liste :", resultat[0])
print("Maximum de la liste :", resultat[1])
print("Minimum de la liste :", resultat[2])

