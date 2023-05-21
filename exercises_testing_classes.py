# Zrób to sam 

# Ćw 11.3. Pracownik

class Employee():
    """Klasa przedstawiająca strukturę pracownika."""

    def __init__(self, name, surname, year_salary = 25000):
        """Przechowuje imię, nazwisko oraz roczny dochód pracownika."""
        self.name = name
        self.surname = surname
        self.year_salary = year_salary

    def give_raise(self):
        """Podnosi dochód pracownika o podaną kwotę."""
        self.year_salary += 5000

        
pracownik = Employee('kamil','kwiek')
pracownik.give_raise()

print(f"Pracownik nazywa się:\n {pracownik.name.title()} {pracownik.surname.title()}, a jego roczny dochód wynosi {pracownik.year_salary}.")       
        
        
# Zestaw testów dla klasy Employee().

import unittest

class TestEmployee(unittest.TestCase):
    """Testy dla klasy Employee."""
    
    def setUp(self):
        """Utworzenie imienia, nazwiska oraz rocznego dochodu dla pracownika."""
        self.employee = Employee('kamil', 'kwiek', 25000)
    
    def test_name_employee(self):
        """Test sprawdzający poprawność imienia pracownika."""
        self.assertEqual(self.employee.name, 'kamil')
        
    def test_surname_employee(self):
        """Test sprawdzający poprawność nazwiska pracownika."""
        self.assertEqual(self.employee.surname, 'kwiek')
        
        
    def test_give_default_raise(self):
        """Test sprawdzający poprawność klasy, przy domyślnej wartości dochodu."""
        self.assertEqual(self.employee.year_salary, 25000)
    
    def test_give_custom_raise(self):
        """Test sprawdzający czy podniesienie dochodu jest poprawne."""
        self.employee.give_raise()
        self.assertEqual(self.employee.year_salary, 30000)
    
    
if __name__ == '__main__':
    unittest.main()        
    
   
    