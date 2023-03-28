# Używanie funkcji wraz z pętlą while

def get_formatted_name(first_name, last_name):
    """Zwraca elegenacko sformatowane pełne imię i nazwisko"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nProszę podać imię i nazwisko: ")
    print("(wpisz 'koniec', aby zakończyć pracę w dowolnym momencie)")
    
    f_name = input("Imię:" ) 
    if f_name == 'koniec':
        break
    l_name = input("Nazwisko:" )
    if l_name == 'koniec':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nWitaj, {formatted_name}!")