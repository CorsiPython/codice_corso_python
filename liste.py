# Scrivi un programma che, con un ciclo while, chieda all utente di inserire numeri interi
# finché non viene inserito il numero 0. Alla fine, stampa la somma di tutti i numeri
# inseriti (escluso lo 0).

somma = 0

while True:
    n = int(input("Inserici un numero oppure 0 per fermarti: "))
    if n == 0:
        break
    
    somma += n

print(somma)