def produit_dans_intervalle(liste, debut, fin):
   
    produit = 1


    for nombre in liste:
        
        if debut <= nombre <= fin:
            produit *= nombre

    return produit


L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]


debut_intervalle = 25
fin_intervalle = 90

resultat = produit_dans_intervalle(L, debut_intervalle, fin_intervalle)


print("Produit des valeurs dans l'intervalle [25, 90] :", resultat)
