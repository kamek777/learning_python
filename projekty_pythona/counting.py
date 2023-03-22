# Użycie polecenia 'continue'

current_number = 0 
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue # Powrót do początku pętli i ominięcie tego etapu, 
                 #więc parzyste liczby nie bierze pod uwage. 
    print(current_number)
    
# CTRL + C - przerywanie pętli    

