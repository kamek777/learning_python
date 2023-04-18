# Zrób to sam

# Ćw 11.1. Miasto, państwo

def country_town(country,town):
    """Prosta funkcja zawierająca informacje o kraju i mieście znajdującym się w nim."""
    return f"{country.title()}, {town.title()}."

print(country_town('polska','warszawa'))

import unittest
from city_functions import country_town

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'city_functions.py'"""
    
    def test_city_country(self):
        city_country = country_town('polska','warszawa')
        self.assertAlmostEqual(city_country, 'Polska, Warszawa.')
        
if __name__ == '__main__':
    unittest.main()        
    
    
# Ćw 11.2. Populacja

def country_town_population(country,town,population=''):
    """Prosta funkcja zawierająca informacje o kraju, mieście oraz populacji."""
    if population:
        return f"{country.title()}, {town.title()} - {population}."
    else:
        return f"{country.title()}, {town.title()}."

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'city_functions_population.py'"""
    
    def test_city_country_population(self):
        city_country_population = country_town_population('polska','warszawa',300000)
        self.assertAlmostEqual(city_country_population, 'Polska, Warszawa - 300000')
        
if __name__ == '__main__':
    unittest.main()            