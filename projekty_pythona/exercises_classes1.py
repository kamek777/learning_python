# Zrób to sam 

# Ćw 9.4 Liczba obsłużonych

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
        
             
             

# Egzemplarze

restaurant = Restaurant('złote gęsi','polska',10)  
print("---")
restaurant.describe_restaurant()
restaurant.open_restaurant()   
restaurant.increment_number_served(8) # dodajemy 8 kolejnych klientów
restaurant.set_number_served()    

# Ćw 9.5 Próby logowania 

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
        
        
user1 = User('kamil','kwiek',22,180) 
user1.describe_user()  

# Sprawdzamy początkową liczbę zalogowań użytkownika:
user1.read_login_attempts()

# Dodajemy liczbę logowań użytkownika o 1
user1.increment_login_attempts()
user1.read_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()

# Resetujemy liczbę logowań:
user1.reset_login_attempts()
user1.read_login_attempts()


     
              
        
        