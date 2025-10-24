# Dato il file lines.txt , scrivi un programma che legge il file e crea un nuovo file chiamato
# lines_numbers.txt in cui ogni riga del file originale è preceduta dal suo numero di riga (a
# partire da 1). Ad esempio, la prima riga del nuovo file dovrebbe essere "1: <contenuto
# della prima riga del file originale>".

with open("lines.txt", 'r') as infile, open("lines_numbers.txt", 'w') as outfile:
    
    for i, line in enumerate(infile):
        outfile.write(f"{i + 1}: {line}")