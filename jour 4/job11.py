def augmenter_liste(liste):

    liste = [nombre + 1 for nombre in liste]
    return liste
L = [7, 11, 42, 39, 2]


nouvelle_liste = augmenter_liste(L)


print("Liste initiale :", L)
print("Liste après augmentation de 1 :", nouvelle_liste)
