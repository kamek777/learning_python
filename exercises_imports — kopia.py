# Zrób to sam 

# Ćw 9.10 Zaimportowana klasa Restaurant

# Importujemy klasę Restaurant():

from exercises_classes1 import Restaurant as R

restaurant1 = R('gąska','polska',10)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
  
# Ćw 9.11 Zaimportowana klasa Admin  
    
from exercises_classes2 import Admin as A, User as U

admin1 = A('kamil','kwiek',22,180)
admin1.show_privileges() 

user1 = U('kamil','kwiek',22,180)
user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()


# Ćw 9.12 Wiele modułów

# Zrobione!