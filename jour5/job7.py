def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
           
            notes_arrondies.append(note)
        else:
          
            prochain_multiple_de_5 = (note // 5 + 1) * 5
            if prochain_multiple_de_5 - note < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies


notes_eleves = [83, 72, 95, 39, 41, 87]
notes_arrondies = arrondir_notes(notes_eleves)


print("Notes originales :", notes_eleves)
print("Notes arrondies   :", notes_arrondies)
