# Scrivi un programma che chieda all'utente di
# inserire un numero intero n e stampi tutti i numeri
# pari da 0 a n
n = int(input("n: "))

for x in range(n + 1):
    if x % 2 == 0:
        print(x)
