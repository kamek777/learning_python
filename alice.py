#Wczytywanie danych z obsługą wyjątku FileNotFoundError
#Analiza tekstu 'Alicja w Krainie Czarów'

filename = 'pliki_tekstowe/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Przepraszamy, ale plik {filename} nie istnieje.")    
else:
    #Obliczenie przybliżonej liczby słów w pliku.
    #Metoda split() dzieli ciąg tekstowy w miejscu występowania spacji.
    words = contents.split()
    num_words = len(words)
    print(f"Plik {filename} zawiera {num_words} słów.")

 