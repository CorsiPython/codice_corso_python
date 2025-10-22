# Scrivi un programma che, data una stringa in input, 
# stampi il numero di vocali presenti nella stringa.

frase = input("Dammi una frase: ")
vocali = "aeiou"
conto = 0

for lettera in frase:
    if lettera in vocali:
        conto += 1

print("Il numero di vocali è:", conto)
