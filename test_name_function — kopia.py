# Testowanie funkcji modułem unittest

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'name_function.py'."""
    
    
    def test_first_last_name(self):
        """Czy dane w postaci 'Jan Kowalski' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_name('jan','kowalski')
        self.assertEqual(formatted_name, 'Jan Kowalski')
        
    def test_first_last_middle_name(self):
        """Czy dane w postaci 'Jan Sebastian Kowalski' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_name('jan','kowalski','sebastian')
        self.assertEqual(formatted_name, 'Jan Sebastian Kowalski')
    
if __name__ == '__main__':
    unittest.main()