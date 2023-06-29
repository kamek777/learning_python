import csv 
import matplotlib.pyplot as plt

filename = 'C:/Users/PC/OneDrive/Pulpit/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
        
    #Pobranie temperatur maksymalnych z pliku
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(highs)
    
    print(highs)
    
#Dane wykresu
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')
    
#Formatowanie wykresu
ax.set_tilte("Najwyższa temperatura dnia, lipiec 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel(axis='both',which='major', fontsize=16)

#Wyświetlenie wykresu
plt.show()
