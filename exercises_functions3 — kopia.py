# Zrób to sam 

# Ćw 8.9 Komunikaty

# Tworzymy listę

komunikaty = ['cześć','witam','halo','ej']
komunikaty1 = komunikaty[:]
# Tworzymy funkcję:

def show_messages(messages):
    for message in messages:
        print(f"Oto nastepujący komunikat:{message.title()},")
        
# Wyświetlamy funkcję

show_messages(komunikaty)
    
    
# Ćw 8.10 Wysyłanie komunikatów

# Tworzymy pustą listę

sent_messages = []

def send_messages(messages):
    while messages:
        for message in messages:
            mess = messages.pop()
            sent_messages.append(mess)
            print(f"Kolejne dodawane komunikaty to: {sent_messages}")
            
send_messages(komunikaty)
#print(sent_messages)
#print(komunikaty)

# Ćw 8.11 Zarchiwizowane komunikaty 
send_messages(komunikaty[:])
print(komunikaty)