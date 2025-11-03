# Scrivi un programma che stampi i numeri da 1 a 100. Per i multipli di 3,
# stampa "Fizz" invece del numero, per i multipli di 5 stampa "Buzz", e per i multipli di
# entrambi (3 e 5) stampa "FizzBuzz".

for n in range(1, 31):
    print(n)
    if n % 3 == 0:
        print("Fizz")
    if n % 5 == 0:
        print("Buzz")
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
