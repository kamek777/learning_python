# Argumenty pozycyjne i przekazywanie dowolnej liczby argumentów

def make_pizza(size,*toppings):
    """Podsumowanie informacji o przygotowanej pizzy."""
    print(f"\nPrzygotowuję pizzę o wielkości {size} cm, z następującymi składnikami: ")
    for topping in toppings:
        print(f"- {topping}")
        
# Tworzymy pizzę wywołując funkcje

make_pizza(40,'pepperoni')
make_pizza(50,'pieczarki','kurczak','zielona papryka','podwójny ser')       

# Często spotykamy się z *args - dowolna liczba argumentów pozycyjnych! 