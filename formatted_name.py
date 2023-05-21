# Wartości zwrotne w funkcjach

def get_formatted_name(first_name,last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

me = get_formatted_name('kamil','kwiek')
print(me)

# Drugi przypadek z wartością domyślną jako pusty łańcuch znaków 
# Middle name jest opcjonalny

def get_formatted_name1(first_name,last_name,middle_name=''):
    """Zwraca elegancko sformatowane pełne imię i nazwisko"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
        
    return full_name.title()

print(get_formatted_name1('jan','bach'))
print(get_formatted_name1('jan','bach','sebastian'))

# Pamiętajmy, że wartości domyślne w funkjach definiujemy na samym końcu!
