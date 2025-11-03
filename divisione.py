a = int(input("Inserisci il dividendo: "))
b = int(input("Inserisci il divisore: "))

while b == 0:
    b = int(input("La divisione per 0 non è possibile! Inserisci un altro numero: "))

print("Il risultato è: ", a / b)
