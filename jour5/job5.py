def chiffrement_cesar(message, decalage):
    resultat = ""

    for caractere in message:
        
        if caractere.isalpha():
            
            majuscule = caractere.isupper()
            
            
            indice = ord(caractere.lower()) - ord('a')

            
            indice_decale = (indice + decalage) % 26

            
            caractere_decale = chr(indice_decale + ord('a'))

            
            if majuscule:
                caractere_decale = caractere_decale.upper()

           
            resultat += caractere_decale
        else:
           
            resultat += caractere

    return resultat


message_original = "Bonjour, Jules César!"
decalage = 
message_decale = chiffrement_cesar(message_original, decalage)

print(f"Message original : {message_original}")
print(f"Message décalé : {message_decale}")
