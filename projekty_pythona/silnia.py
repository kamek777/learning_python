#Funkcja tworząca silnie z danej liczby
def silnia(n):
    """Tworzymy instancję funkcji silnia."""
    if n>1:
        return n*silnia(n-1)
    return 1

#Przykład użycia
print(silnia(5))