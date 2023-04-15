# Program, witający użytkownika zapisanego w pliku JSON (wczytując go).

import json
filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Witamy ponownie, {username}!")