# Zrób to sam 

# Ćw 8.3 T-shirt

# Definiujemy funkcję, gdzie argumentami będzie informacja o rozmiarze oraz tekscie na t-shirt'ie

def make_shirt(rozmiar,nadruk):
    print(f"Twoja zamówiona koszulka jest rozmiaru {rozmiar} z napisem {nadruk}.")

# Wywołanie naszej funkcji

# Argumenty pozycyjne:
make_shirt(32,'Adidas')    

# Argumenty w postaci słów kluczowych:
make_shirt(rozmiar='34',nadruk='Nike')

# Ćw 8.4 Duże koszulki

def make_shirt1(rozmiar='duża',nadruk='Uwielbiam Pythona'):
    print(f"Twoja zamówiona koszulka jest rozmiaru {rozmiar} z napisem {nadruk}.")
    
# Wywołanie funkcji z argumentami domyślnymi
make_shirt1()    

make_shirt1(rozmiar='średni')

make_shirt1(nadruk='Python to mój ulubiony język')

# Ćw 8.5 Miasta 

# Tworzymy funkcję, która wyświetlać będzie komunikat o danym kraju i mieście

def describe_city(miasto,kraj='Polska'):
    print(f"{miasto.title()} leży w kraju {kraj.title()}.")
    
# Wywołanie funkcji   

describe_city('kraków')  

# Dla 3 różnych miast:
describe_city('poznań')
describe_city('warszawa')

# Jedno miasto nie leżące w domyślnym kraju
describe_city('paryż')