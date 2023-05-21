# Odczytywanie danych z pliku

#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#print(contents.rstrip())

# metoda rstrip() powoduje usunięcie pustego wiersza (białe znaki), jeśli takoby występował

# Ścieżka dostępu do pliku 

with open('pliki_tekstowe/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# Wykorzystanie iteracji przy użyciu pętli for do odczytania pliku 'wiersz po wierszu':
filename = 'pliki_tekstowe/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
# Utworzenie listy wierszy na podstawie zawartości pliku przy pomocy metody readlines():

filename = 'pliki_tekstowe/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())        