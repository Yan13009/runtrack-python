
montant_initial = 10000.0  
taux_rendement_annuel = 5.0  


def calculer_gain_annuel(montant, taux_rendement):
    return (taux_rendement / 100) * montant


gain_annuel_initial = calculer_gain_annuel(montant_initial, taux_rendement_annuel)
print(f"Gain annuel initial : {gain_annuel_initial} euros")


montant_initial += 5000
taux_rendement_annuel += 2.0


gain_annuel_apres_augmentation = calculer_gain_annuel(montant_initial, taux_rendement_annuel)
print(f"Gain annuel après augmentation du capital et du taux de rendement : {gain_annuel_apres_augmentation} euros")


retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1.0


montant_final = montant_initial + gain_annuel_apres_augmentation
nouveau_gain_annuel = calculer_gain_annuel(montant_final, taux_rendement_annuel)
print(f"Montant final de l'investissement : {montant_final} euros")
print(f"Nouveau gain annuel après retrait et diminution du taux de rendement : {nouveau_gain_annuel} euros")
