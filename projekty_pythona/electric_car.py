# Dziedziczenie klas 

# Klasa nadrzędna
class Car():
    """Prosta próba zaprezentowania samochodu."""
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0 
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")
        
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")
            
    def increment_odometer(self,kilometers):
        self.odometer_reading += kilometers
        
# Klasa potomna (podrzędna) 
class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""
    
    def __init__(self,make,model,year):
        """Inicjalizacja atrybutów klasy nadrzędnej."""
        super().__init__(make,model,year)

# Funkcja super() umożliwia połączenie między klasą nadrzedną a potomną!

my_tesla = ElectricCar('tesla','model s', 2020)
print(my_tesla.get_descriptive_name())                               