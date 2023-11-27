def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("Les dimensions doivent être supérieures à 1.")
        return

   
    print('|' + '-' * (width - 2) + '|')

  
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

   
    if height > 1:
        print('|' + '-' * (width - 2) + '|')


draw_rectangle(10, 3)
