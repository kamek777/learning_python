"""Obsługiwanie wyjątku ZeroDivisionError"""

print("Podaj dwie liczby, które zostaną podzielone.")
print("Wpisz 'q', aby zakończyć działanie programu.")

# Tworzymy pętlę while
while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("\nDruga liczba: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")    
        
    else:
        print(f"\nWynik dzielenia: {answer}")