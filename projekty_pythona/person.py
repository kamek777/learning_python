# Zwrot słownika w funkcjach

def build_person(first_name,last_name):
    """ Zwraca słownik informacji o danej osobie"""
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person

# Wywołanie funkcji
print(build_person('michael','jordan'))

# Modyfikacja funkcji o wiek, wartość None nie przypisuje żadnej konkretnej wartości

def build_person1(first_name,last_name,age=None):
    """ Zwraca słownik informacji o danej osobie"""
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age:
        person['age'] = age
    return person

# Wywołanie funckji 

player = build_person1('michael','jordan', age = 48)
print(player)