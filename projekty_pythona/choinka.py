# Ustawienie liczby poziomów
levels = 5

# Pętla po poziomach
for level in range(levels):
    # Obliczenie liczby spacji w każdym wierszu
    spaces = levels - level - 1
    
    # Wypisanie spacji
    print(' ' * spaces, end='')
    
    # Obliczenie liczby gwiazdek w każdym wierszu
    stars = 2 * level + 1
    
    # Wypisanie gwiazdek
    print('*' * stars)