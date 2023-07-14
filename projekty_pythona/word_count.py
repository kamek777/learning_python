# Plik z funkcją zliczającą słowa w książkach
def count_word(filename):
    """Obliczenie przybliżonej liczby słów w danym pliku."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass #'Ciche niepowodzenie'
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Plik {filename} zawiera {num_words} słów.")    
        
filename = 'pliki_tekstowe/alice.txt' 
count_word(filename)      

#Tworzymy listę z 3 plikami z różnymi książkami:
filenames = ['pliki_tekstowe/alice.txt','pliki_tekstowe/the_happy_prince.txt','pliki_tekstowe/the_jungle_book.txt']

#Używamy funkcji zliczającej słowa w każdej poszczególnej książce, przy pomocy iteracji.
for filename in filenames:
    count_word(filename)
