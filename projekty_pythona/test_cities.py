import unittest
from city_functions import country_town

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'city_functions.py'"""
    
    def test_city_country(self):
        city_country = country_town('polska','warszawa')
        self.assertAlmostEqual(city_country, 'Polska, Warszawa.')
        
if __name__ == '__main__':
    unittest.main()        