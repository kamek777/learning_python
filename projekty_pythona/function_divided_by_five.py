#Zdefiniowanie funkcji
def divided_by_five(lista):
    count = 0 
    for element in lista:
        if element % 5 == 0 and element < 100: 
            count += 1
        elif element > 100:
            return 0
    return count
        
#Stworzenie nowej listy
nowa_lista = [5,10,23,33,99]

#Wyświetlenie
print(divided_by_five(nowa_lista))