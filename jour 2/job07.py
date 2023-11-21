def pyramid_sequence(input_string, levels):
    for i in range(1, levels + 1):
        print(input_string[:i].center(levels * 2 - 1))

input_string = "abcdefghijklmnopqrstuvwxyz"


number_of_levels = 15


pyramid_sequence(input_string, number_of_levels)
