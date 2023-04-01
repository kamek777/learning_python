# Zró to sam

# Ćw 9.1 Restauracja

# Tworzymy klasę 

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,hours):
        """Inicjalizacja atrybutów"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.hours = hours
        
    def describe_restaurant(self):
        """Metoda wyświetlająca nazwę restauracji oraz rodzaj jej kuchni""" 
        print(f"Restauracja ta nazywa się: {self.restaurant_name.title()}.") 
        print(f"Jest to kuchnia {self.cuisine_type.title()}.")  
              
    def open_restaurant(self):
        """Metoda wyświetlająca ilość goin pracy restauracji"""  
        print(f"Restauracja jest czynna {self.hours} godzin.")   
             
# Tworzenie egzemplarzu

restaurant = Restaurant('złote gęsi','polska',10) 
restaurant.describe_restaurant() 
restaurant.open_restaurant()

# Utworzenie 3 nowych egzemplarzy 

restaurant1 = Restaurant('małe strusie','grecka',8) 
restaurant2 = Restaurant('beauty small','amerykańska',10)
restaurant3 = Restaurant('french apples','francuska',9)  

# Wywołanie na nich metod utworzonych powyżej

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()       