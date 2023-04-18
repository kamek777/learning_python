# Testowanie funkcji przy pomocy modułu unittest.
def get_formatted_name(first,last,middle=''):
    """Generuje sformatowane pełne imię i nazwisko użytkownika."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
    
print(get_formatted_name('jan','sebastian','kowalski'))