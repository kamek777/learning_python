# Przekazywanie dowolnej liczby argumentów
# *argument - oznacza, że możemy dodawać ile chcemy argumentów

def make_pizza(*toppings):
    """Wyświetla listy dodatków wybranych przez klienta."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('pieczarki','zielona papryka','podwójny ser')    

# Ta sama metoda przy użyciu iteracji

def make_pizza1(*toppings):
    """ Podsumowanie informacji o przygotowanej pizzy."""
    for topping in toppings:
        print(f"+{topping}")
        
make_pizza1('pepperoni') 
make_pizza1('pieczarki','zielona papryka','podwójny ser')  

# Argumenty pozycyjne i przekazywanie dowolnej liczby argumentów     