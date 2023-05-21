#prompt = "\n Powiedz mi coś o sobie: "
#prompt += "\n Wpisz 'koniec' jeśli chcesz przerwać."
#message = ""

#while message != 'koniec':
    #message = input(prompt)
    #print(message)
    
    #if message != 'koniec':
        #print(message)
        
# Tworzenie flagi w programie 
 
prompt = "\n Powiedz mi coś o sobie: "
prompt += "\n Wpisz 'koniec' jeśli chcesz przerwać."

# Flaga:

active = True 
while active:
    message = input(prompt)
    
    if message == 'koniec':
        active = False
    else:
        print(message)           