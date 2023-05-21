# Tworzymy klasę zawierającą informacje o samochodach oraz ich przebiegu

class Car():
    """Prosta próba zaprezentowania samochodu"""
    
    def __init__(self,make,model,year,mileage=0):
        """Inicjalizacja atrybutów opisujących samochód."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = mileage
       
    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu."""
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")
        
    def update_odometer(self, mileage):
        """Przypisanie podaje wartości licznikowi przebiegu". Zmiana zostanie odrzucona w przypadku
        próby cofnięcia licznika."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")   
    # Inkrementacja wartości atrybutu za pomocą metody
    
    def increment_odometer(self,kilometers):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną wartość."""
        if kilometers >= 0:
            self.odometer_reading += kilometers
        else:
            print("Nie możemy podać ujemnej wartości przebiegu!")    
        
        
        
my_new_car = Car('audi','a4',2019)    
print(my_new_car.get_descriptive_name())

# Wywołanie atrybutu z wartością domyślną:
#my_new_car.read_odometer()

# Bezpośrednia modyfikacja wartości atrybutu 

#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

# Modyfikacja wartości artybutu za pomocą metody

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100) # Dodanie 100 km do przebiegu
my_new_car.read_odometer() # Odświeżenie przebiegu z dodanymi 100 