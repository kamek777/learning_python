# Zrób to sam 

# Ćw 6.8 Nazwy miast 

def city_country(city,country):
    connection = f"{city}, {country}"
    return connection.title()
print(city_country('cracow','poland'))
print(city_country('paris','france'))
print(city_country('london','england'))
  
  
  
# Ćw 8.7 Album   

def make_album(zespol_wykonawca,tytul_albumu,liczby_utworow=None):
    album = {'zespol/wykonawca': zespol_wykonawca, 'tytul': tytul_albumu}
    if liczby_utworow:
        album['liczby_utworow']=liczby_utworow
    return album    
    


# Stworzenie 3 słowników:

first = make_album('paktofonika','jestem bogiem')
second = make_album('nirvana','kwiatki') 
third = make_album('piotr kubicha', 'szalenstwo')  

# Przedstawienie słowników:

print(first)
print(second)
print(third)  

# Utworzeni czwartego słownika z dodatkiem liczby plyt:

fourth = make_album('coldplay','paradise',liczby_utworow=3)
print(fourth)

    
# Ćw 8.8 Albumy użytkowników

while True:
    print("\n Podaj artystę oraz tytuł piosenki (jeśli chcesz zakończyć pracę wpisz 'koniec'): ")
    artysta = input("\nPodaj artystę: ")
    tytul = input("\nPodaj tytuł piosenki: ")
    if artysta == 'koniec':
        break
    if tytul == 'koniec':
        break    
    
    nowy_album = make_album(artysta,tytul)
    
print(f"Oto nowo utworzony album: {nowy_album}")    
    