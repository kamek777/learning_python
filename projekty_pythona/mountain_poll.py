# Umieszczenie w słowniku danych wejściowych wprowadzonych przez użytkownika 

responses = {}

# Ustawienie flagi 

polling_active = True 

while polling_active:
    name = input("Jak masz na imię? ") # Klucz 
    response = input("Na który szczyt chciałbyś się wspiąć pewnego dnia? ") # Wartość
    
# Umieszczenie odpowiedzi w słowniku 
responses[name] = response

# Ustalenie czy ktoś chce jeszcze wziąć udział w ankiecie 

repeat = input("Czy ktoś chce jeszcze wziąć udział w ankiecie? ('tak'/'nie')?")

if repeat == 'nie':
    polling_active = False 
    
# Po zakończeniu ankiety wyświetlamy jej wyniki:
print("---Wyniki ankiety---")
for name,response in responses.items():
    print(f"{name} chciałby/chciałaby wspiąć się na {response}")    
