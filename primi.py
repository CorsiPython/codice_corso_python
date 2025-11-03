# Scrivi un programma che chiede all'utente di 
# inserire un numero intero positivo
# stampa tutti i numeri primi minori o uguali a n.

import prime_functions

n = int(input("n: "))

if n <= 0:
    raise ValueError("Il numero deve essere positivo!")

for x in range(n+1):
    if prime_functions.is_prime(x):
        print(x)