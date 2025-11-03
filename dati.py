# Il file dati.csv (disponibile su Classroom) contiene dati separati da virgole. La prima
# riga è l'intestazione con i nomi delle colonne, e le righe successive contengono i dati.
# Scrivi un programma che legge il file dati.csv e lo trasforma in un dizionario di liste,
# dove ogni chiave è il nome di una colonna e il valore è una lista dei dati corrispondenti
# a quella colonna.

colonna = input("Insersci una colonna su cui fare la media: ")

with open("dati.csv", 'r') as file:
    
    righe = [riga.strip() for riga in file.readlines()]
    
    header = righe[0].split(",")
    content = righe[1:]

    dati = {attributo : []
            for attributo in header
            }

for i, record in enumerate(content):

    record = record.split(",")

    for attributo, dato in zip(header, record):
        dati[attributo].append(int(dato))
        

if not colonna in dati:
    raise ValueError("L'attributo non è valido")

somma = 0
for dato in dati[colonna]:
    somma += dato

media = somma / len(dati[colonna])

print(f"la media di `{colonna}` è {media}")