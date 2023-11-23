def main():
    L = [1, 2, 3, 4, 5]

    print("Deuxième valeur de la liste :", L[1])

    L[3] = L[2] + L[4]

    print("Tableau après la modification :", L)
    print("Dernière valeur de la liste :", L[-1])

if __name__ == "__main__":
    main()
