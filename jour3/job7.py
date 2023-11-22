import sys

def determiner_specialite(langage):
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

# Vérifiez si des arguments de ligne de commande ont été fournis
if len(sys.argv) > 1:
    langage = sys.argv[1]
    determiner_specialite(langage)
else:
    print("Veuillez fournir un langage en argument de la ligne de commande.")
