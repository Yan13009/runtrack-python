def compter_multiples_de_trois(liste):
    
    count = 0

   
    for nombre in liste:
       
        if nombre % 3 == 0:
            count += 1

    return count


L = [8, 24, 48, 2, 16]

resultat = compter_multiples_de_trois(L)


print("Nombre de multiples de 3 dans la liste :", resultat)
