# Crea un dizionario chiamato frutta_prezzi
# "mela": 0.5
# "banana": 0.3
# "arancia": 0.7
#  che contenga i seguenti elementi:

# Usa il dizionario frutta_prezzi per calcolare il costo totale di un
# carrello della spesa che
# contiene:
# 3 mele
# 2 banane
# 5 arance

frutta_prezzi = {"mela": 0.5, "banana": 0.3, "arancia": 0.7}

frutta = [
    "mela",
    "mela",
    "mela",
    "banana",
    "banana",
    "arancia",
    "arancia",
    "arancia",
    "arancia",
    "arancia",
]

prezzo = 0
for frutto in frutta:
    prezzo += frutta_prezzi[frutto]

print(prezzo)

print(sum(map(lambda frutto: frutta_prezzi[frutto], frutta)))

# stampa tutti i frutti diversi nel carrello
print(set(frutta))
