# Dato il file lines.txt , scrivi un programma che legge il
# contenuto del file, e scrive in un
# nuovo file chiamato reversed_lines.txt tutte le righe
# del file originale, ma con l'ordine
# delle righe invertito
# (l'ultima riga diventa la prima,
# la penultima diventa la seconda, e
# così via).

with open("lines.txt", "r") as f:
    righe = f.readlines()

righe_pulite = []
for riga in righe:
    riga_pulita = riga.strip()
    riga_pulita = f"{riga_pulita}\n"
    righe_pulite.append(riga_pulita)

with open("reversed_lines.txt", "w") as f:
    f.write("".join(list(reversed(righe_pulite))))
