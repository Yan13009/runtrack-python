while True:
    try:
      
        N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))

     
        if N <= 0:
            raise ValueError("Veuillez saisir un entier supérieur à zéro.")
        
       
        for i in range(1, N + 1):
            print(f"\nTable de multiplication de {i} :")
            for j in range(1, 11):
                resultat = i * j
                print(f"{i} * {j} = {resultat}")

      
        break

    except ValueError:
        print("Erreur : Veuillez saisir un entier valide.")
