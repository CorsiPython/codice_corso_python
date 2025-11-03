# Dato il file lines.txt , scrivi un programma che legge il file e conta quante righe
# contengono almeno una vocale (a, e, i, o, u, sia maiuscole che minuscole). Stampa il
# conteggio totale delle righe con almeno una vocale.

conto = 0
vocali = list("aeiou")


with open("lines.txt", "r") as file:
    for line in file:
        for vocale in vocali:
            if vocale in line.lower():
                conto += 1
                break

print(f"Il numero di righe con almeno una vocale è: {conto}")
