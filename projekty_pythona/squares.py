# Kwadraty poszczególnych elementów w liscie
kwadraty = []
for kwadrat in range(1,11):
	squares = kwadrat**2
	kwadraty.append(squares)
print(kwadraty)	

# II sposób na ten samo kod (listy składane)
kwadraty = [kwadrat**2 for kwadrat in range(1,11)]

print(kwadraty)