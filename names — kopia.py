from name_function import get_formatted_name

print("Wpisz 'q', aby zakończyć działanie programu.")

while True:
    first = input("\nPodaj imię: ")
    if first == 'q':
        break
    last = input("\nPodaj nazwisko: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first,last)
    print(f"\tElegancko sformatowane pełne imię i nazwisko: {formatted_name}")
