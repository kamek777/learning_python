filename = 'pliki_tekstowe/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()
    
# Sprawdzenie czy w liczbie pi znajduje się data urodzenia użytkownika
birthday = input("Podaj datę urodzenia (w formacie ddmmrr): ")
if birthday in pi_string:
    print("Twoja data urodzenia znajduje się wśród liczby pi!")
else:
    print("Niestety Twoja data urodzenia nie znajduję się wśród liczby pi :( ")

  