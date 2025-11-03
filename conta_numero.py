# Scrivi un programma al cui interno è predefinita una lista numeri , l'utente deve
# inserire un numero intero n . Il programma deve contare quante volte n appare nella
# lista e stampare il risultato.

numeri = [4, 5, 2, 7, 2, 3, 4, 5, 7, 2]

n = int(input("Numero da cercare: "))

conto = 0

for x in numeri:
    if x == n:
        conto += 1

print(conto)
