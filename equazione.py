# Scrivi un programma che, dati i coefficienti a , b e c
# di un'equazione di secondo
# grado della forma ax^2 + bx + c = 0 , calcoli e stampi
# le soluzioni reali dell'equazione.
# Gestisci il caso in cui le soluzioni non siano reali
# (basta stampare un messaggio di
# errore).

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = (b**2) - 4 * a * c

if delta < 0 or a == 0:
    print("Error!!!")
else:
    x1 = -b + delta ** (1 / 2)
    x1 = x1 / (2 * a)

    x2 = -b - delta ** (1 / 2)
    x2 = x2 / (2 * a)
    print("Le due soluzioni sono")
    print("x1: ", x1)
    print("x2: ", x2)
