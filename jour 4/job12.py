def tri_croissant(liste):
   
    if not liste or len(liste) == 1:
        return liste

   
    for i in range(len(liste)):
        for j in range(0, len(liste)-i-1):
            if liste[j] > liste[j+1]:
                
                liste[j], liste[j+1] = liste[j+1], liste[j]

    return liste


ma_liste = [52, 28, 42, 2, 6]


print("Liste avant le tri :", ma_liste)


liste_triee = tri_croissant(ma_liste)


print("Liste triée :", liste_triee)
