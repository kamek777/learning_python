# Usunięcie z listy danego elementu nawet jeśli jest zawarty kilka razy przy pomocy pętli while

# Tworzymy listę zawierającą zwierzętw
pets = ['pies','kot','pies','złota rybka','kot','królik','kot']

# Wyświetlamy listę
print(pets)

# Usuwamy dany element z listy dopóki nie zniknie całkowicie:
while 'kot' in pets:
    pets.remove('kot') # funkcja remove() usuwa dany element z listy jeden raz
    

# Wyświetlamy nowo edytowaną listę bez kota
print(pets)
# OK