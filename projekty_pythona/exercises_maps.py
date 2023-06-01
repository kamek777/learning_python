#Zrób to sam 

#Ćw 15.1. Sześciany

import matplotlib.pyplot as plt

x_values = range(50001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap= plt.cm.Reds, s=10)

#Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Sześciany liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Sześciany liczb",fontsize=14)

#Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both',which='major',labelsize=14)

#Pokazanie wykresu
plt.show()
