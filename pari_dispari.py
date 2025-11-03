# Scrivi un programma che, data una lista di numeri interi (usa un for con input() per
# popolare la lista), sommi tutti i numeri pari e sottragga tutti i numeri dispari. Stampa il
# risultato finale.

lista = []

for _ in range(10):
    lista.append(int(input("Inserisci un numero: ")))

# Abbiamo una lista piena di numeri!

somma = 0

for n in lista:
    if n % 2 == 0:
        somma += n
    else:
        somma -= n

print("Totale: ", somma)
