def my_long_word(n, phrase):
    mots = phrase.split()
    result = ""

    for mot in mots:
        mot_pur = ""
        for char in mot:
            # Ignorer la ponctuation
            if char.isalpha():
                mot_pur += char
        if len(mot_pur) > n:
            result += mot_pur + " "

    return result.strip()

# Exemple d'utilisation
output = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(output)
