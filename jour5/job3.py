def draw_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            print(spaces + '_')
        elif i == height - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print(spaces + '/' + ' ' * (2 * i) + '\\')


hauteur = int(input("Entrez la hauteur du triangle : "))


draw_triangle(hauteur)
