# Zrób to sam 
# Ćw.1
goscie = ["marek aureliusz", "adam małysz", "jan nowak"]
print(f"Zapraszam do mnie na przepyszny obiad, {goscie[0].title()}!")
print(f"{goscie[1].title()}, kiedy wpadniesz do mnie na obiad?")
print(f"Chętnie zjadłbym z Tobą obiad, {goscie[2].title()}.")
# Ćw.2
print(f"Niestety na mój obiad nie przyjdzie {goscie[2].title()}. ")
# Usunięcie Jana Nowaka z listy i dodanie nowego gościa
goscie = ["marek aureliusz", "adam małysz", "jan nowak"]
print(goscie)
goscie[2] = 'janosik'
print(goscie)
print(f"Zapraszam do mnie na przepyszny obiad, {goscie[0].title()}!")
print(f"{goscie[1].title()}, kiedy wpadniesz do mnie na obiad?")
print(f"Chętnie zjadłbym z Tobą obiad, {goscie[2].title()}.")
# Ćw.3
print("Znaleźlismy nowe osoby na obiad!")
goscie.insert(0,'Abba')
print(goscie)
goscie.insert(2,'Król Artur')
print(goscie)
goscie.append('Królowa Jadwiga')
print(goscie)
print(f"Zapraszam na obiad, {goscie[0]}.")
print(f"Zapraszam na obiad, {goscie[1].title()}.")
print(f"Zapraszam na obiad, {goscie[2]}.")
print(f"Zapraszam na obiad, {goscie[3].title()}.")
print(f"Zapraszam na obiad, {goscie[4].title()}.")
print(f"Zapraszam na obiad, {goscie[5]}.")
print(goscie)
print("Niestety mogę zaprosić tylko dwie osoby :( ")
usuniety_gosc_1 = goscie.pop()
print(f"Przepraszam za brak miejsc, {usuniety_gosc_1}.")
usuniety_gosc_2= goscie.pop()
print(f"Przepraszam za brak miejsc, {usuniety_gosc_2.title()}.")
usuniety_gosc_3 = goscie.pop()
print(f"Przepraszam za brak miejsc, {usuniety_gosc_3.title()}.")
usuniety_gosc_4 = goscie.pop()
print(f"Przepraszam za brak miejsc, {usuniety_gosc_4}.")
print(goscie)


