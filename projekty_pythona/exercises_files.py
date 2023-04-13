# Zrób to sam

# Ćw 10.1. Poznajemy Pythona

filename = 'pliki_tekstowe/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)   

with open(filename) as file_object:
    for line in file_object:
        print(line) 
        
with open('pliki_tekstowe/learning_python.txt') as file_object:
    contents = file_object.read()
    
print(contents)    

# Ćw 10.2. Poznajemy C

print(contents.replace('pythonie','Javie')) 