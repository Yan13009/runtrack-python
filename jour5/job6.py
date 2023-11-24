def distance_to_toilet(marches, hauteur_marche):
    nombre_de_marches_aller_retour = marches * 2  # Aller et retour à chaque passage aux toilettes
    distance_par_marche_aller_retour = hauteur_marche * nombre_de_marches_aller_retour

    distance_par_jour = distance_par_marche_aller_retour * 5  # 5 passages par jour
    distance_par_semaine = distance_par_jour * 7  # 7 jours par semaine

    distance_en_metres = distance_par_semaine / 100  

    return distance_en_metres


nombre_de_marches = 10
hauteur_marche = 20

distance_parcourue = distance_to_toilet(nombre_de_marches, hauteur_marche)


print(f"Pour {nombre_de_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_parcourue:.2f} m par semaine.")
