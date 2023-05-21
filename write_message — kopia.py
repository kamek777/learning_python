# Zapisywanie danych do pustego pliku

filename = 'pliki_tekstowe/programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("Uwielbiam programowac!\n")
    file_object.write("Zwlaszcza w pyhonie.\n")
    file_object.write("Uwielbiam odnajdywac elementy w ogromnych zbiorach danych.")
    
# 'w' nadpisuje ciąg znaków, 'a' dodaje kolejne bez usunięcia poprzednich ciągów    