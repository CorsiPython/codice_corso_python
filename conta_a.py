# Dato il file lines.txt (è Su Classroom!), scrivi un programma che conta tutte le
# lettere 'a' (sia maiuscole che minuscole) presenti nel file
# e stampa il conteggio totale.

count = 0

with open("lines.txt", "r") as file:
    contenuto = file.read()

    for lettera in contenuto:
        if lettera.lower() == "a":
            count += 1

print(f"In lines.txt ci sono {count} lettere a.")
