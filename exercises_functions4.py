# Zrób to sam

# Ćw 8.12 Kanapki

def zamowienia(*skladniki):
    for skladnik in skladniki:
        print(f"-{skladnik}")
        
print("Oto Twoje składniki z zamówienia: ")   
zamowienia('woda','jajecznica','kotlet schabowy z ziemniakami')     

# Ćw 8.13 Profil użytkownika

def build_profile(first,last,**user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = build_profile('kamil','kwiek',lokalizacja = 'Kraków', 
                             wiek = 22, ulubione_hobby = 'siłownia')
print(user_profile)

# Ćw 8.14 Samochody

def make_car(name,model,**car_info):
    car_info['name_car'] = name.title()
    car_info['model_car'] = model.title()
    return car_info

print(make_car('BMW','m4',color='gold',tow_package=True,nitro=True))