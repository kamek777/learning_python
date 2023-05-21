# Argumenty pozycyjne 

def describe_pet(animal_type,pet_name):
    """Wyświetla informacje o zwierzęciu"""
    print(f"\nMoje zwierzę to: {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")

# Wywołanie funkcji 

describe_pet('kot','ksawery')    

# Wiele wywołań funkcji 

describe_pet('pies','korneliusz')
describe_pet('jaszczurka','tomek')    
    

# Argumenty w postaci słów kluczowych 

def describe_pet2(animal_type,pet_name):
    """ Wyświetla informacje o zwierzęciu"""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")
    
describe_pet2(animal_type='chomik',pet_name='harry')    


# Wartości domyślne w funkcjach

def describe_pet3(pet_name,animal_type='pies'):
    """ Wyświetla informacje o zwierzęciu z wartością domyślną pies"""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")

describe_pet3(pet_name='willie')    
describe_pet3('kornelia')

# Wartości domyślne na samym końcu!!!
