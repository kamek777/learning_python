def make_pizza(size,*toppings):
    """Podsumowanie informacji o przygotowanej pizzy."""
    print(f"\nPrzygotowuję pizzę o wielkości {size} cm, z następującymi składnikami: ")
    for topping in toppings:
        print(f"- {topping}")
        