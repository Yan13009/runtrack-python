def echanger_premiere_et_derniere(liste):
 
    if liste:
       
        liste[0], liste[-1] = liste[-1], liste[0]


ma_liste = [1, 2, 3, 4, 5]
print("Liste avant l'échange :", ma_liste)


echanger_premiere_et_derniere(ma_liste)


print("Liste après l'échange :", ma_liste)
