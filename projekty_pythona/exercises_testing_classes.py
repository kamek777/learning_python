# Zrób to sam 

# Ćw 11.3. Pracownik

class Employee():
    """Klasa przedstawiająca strukturę pracownika."""
    
    def __init__(self,name,surname):
        """Przechowuje imie, nazwisko oraz roczny dochód pracownika."""
        self.name = name
        self.surname = surname
        self.year_salary = []
        
    def give_raise(self):
        """Podnosi dochód pracownika domyślnie o 5000 zł."""
        self.year_salary = 5000
        
employee = Employee('kamil','kwiek')
employee.give_raise()
print(employee)        
        
        
    