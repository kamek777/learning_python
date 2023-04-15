# Używanie json.dump() oraz json.load() do przechowywania danych

import json

#Zapisanie
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers,f)
    
#Wczytanie
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)    