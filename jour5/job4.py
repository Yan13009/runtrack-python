def draw_diagonal_carpet(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print('/', end='')
            elif i == n - j:
                print('\\', end='')
            else:
                print('_', end='')
        print()


taille = 10
draw_diagonal_carpet(taille)
