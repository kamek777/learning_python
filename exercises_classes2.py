# Zrób to sam 

# Ćw 9.6 Budka z lodami 

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,hours):
        """Inicjalizacja atrybutów"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.hours = hours
        self.number_served = 10
        
    def describe_restaurant(self):
        """Metoda wyświetlająca nazwę restauracji oraz rodzaj jej kuchni.""" 
        print(f"Restauracja ta nazywa się: {self.restaurant_name.title()}.") 
        print(f"Jest to kuchnia {self.cuisine_type.title()}.")  
              
    def open_restaurant(self):
        """Metoda wyświetlająca ilość goin pracy restauracji."""  
        print(f"Restauracja jest czynna {self.hours} godzin.")   
    
    def set_number_served(self):
        """Wyświetla liczbę obsłużonych klientów."""   
        print(f"Oto liczba obsłużonych klientów: {self.number_served}.")
        
    def increment_number_served(self,client):
        self.number_served += client
        
        
# Tworzenie klasy potomnej

class IceCreamStand(Restaurant):
    """Klasa potomna klasie nadrzędnej Restaurant zawierająca wszystkie elementy dla budki z lodami."""
    
    def __init__(self,restaurant_name,cuisine_type,hours):
        """Inicjalizacja atrybutów klasy nadrzędnej."""
        super().__init__(restaurant_name,cuisine_type,hours)
        
        
    def read_flavors(self):
        smaki = ['truskawka','wanilia','czekolada','banan','malina']  
        print("\nDostępne smaki lodów to: ")
        for i in smaki:
            print(f"-{i},")
        
# Stworzenie egzemplarza:
lod1 = IceCreamStand('casino','włoska',10,)

# Wywołanie nowej metody:
lod1.read_flavors()
        
# Ćw 9.7 Admin  
        
class User(): 
    def __init__(self,first_name,last_name,age,height,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = login_attempts
        
        
    
    
    def describe_user(self):
        """Metoda wyświetlająca informacje na temat użytkownika."""    
        user_info = f"Użytkowik to: {self.first_name.title()} {self.last_name.title()}, wiek :{self.age}, wzrost: {self.height}, liczba logowań: {self.login_attempts}"
        print(user_info)
    
    def greet_user(self):
        """Metoda generująca spersonalizowane powitanie dla każdego użytkownika.""" 
        print(f"Witaj, {self.first_name.title()} :)")
        
    def read_login_attempts(self):
        """Metoda wyświetlająca liczbę logowań użytkownika."""
        print(f"Liczba wejść użytkownika {self.first_name.title()} wynosi {self.login_attempts}")
    
    def increment_login_attempts(self):
        """Metoda inkrementująca wartość logowań użytkowników."""
        self.login_attempts += 1
        
    
    def reset_login_attempts(self):
        """Metoda resetująca wartość logowań użytkowników."""
        self.login_attempts = 0          

class Admin(User):
    """Inicjalizacja modelowania admina jako użytkownika danej strony."""
    def __init__(self, first_name, last_name, age, height, login_attempts=0):
        """Inicjalizacja klasy podrzędnej"""
        super().__init__(first_name, last_name, age, height, login_attempts=login_attempts)
        self.privileges = ['może dodać post','może usunąć post', 'może zbanować użytkownika']
    
    def show_privileges(self):
        """Atrybut pokazujący co może zrobić admin."""
        print(f"\nAdmin {self.first_name.title()} ma możliwości następujące: ")
        for i in self.privileges:
            print(f"-{i},")
        
        
# Tworzenie egzemplarzu:

admin1 = Admin('kamil','kwiek',22,180)
admin1.show_privileges()          
        

# Ćw 9.9 Uaktualnienie akumulatora     

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
        
class Battery():
    """Prosta próba modelowania akumulatora samochodu elektrycznego."""
    
    def __init__(self,battery_size=75):
        """Inicjalizacja atrybutów akumulatora."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWm.")          
    
    def get_range(self):
        """Wyświetla informacje o zasięgu samochodu na podstawie pojemności akumulatora."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"Zasięg tego samochodu wynosi około {range} km po pełnym naładowaniu akumulatora.")
    
    def upgrade_battery(self):  
        """Aktualizuje pojemność baterii (ładuje)""" 
        if self.battery_size != 100:
            self.battery_size = 100
        return self.battery_size    
             
        
           

# Klasa potomna (podrzędna) 
class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""
    
    def __init__(self,make,model,year):
        """Inicjalizacja atrybutów klasy nadrzędnej oraz dodanie nowych atrybutów do klasy potomnej."""
        super().__init__(make,model,year)
        self.battery = Battery()   

    def describe_battery(self):
        """Wyświetla informacje o wielkości akumulatora."""
        print(f"Ten samochod ma akumulator o pojemności {self.battery_size} kWh.")
     
    def fill_gas_tank():
        """Samochód o napędzie elektrycznym nie ma zbiornika paliwa."""
        print("Ten samochód nie wymaga tankowania paliwa!")    
           
           
car1 = ElectricCar('audi','a7',2012)   
car1.battery.get_range()
car1.battery.upgrade_battery() 
car1.battery.get_range()
           