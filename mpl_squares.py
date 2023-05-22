import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

#Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość",fontsize=14)
ax.set_ylabel("Kwadraty wartości",fontsize=24)

#Zdefiniowanie wielkości etykiet.
ax.tick_params(axis='both',labelsize=14)

#Pokazanie wykresu
plt.show()