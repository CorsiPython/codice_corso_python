
frase = input("Inserisci una frase: ")

frequenze = {c : frase.lower().count(c) for c in set(frase.lower())}
vocali = set("aeiou")

c_vocali = 0
c_consonanti = 0
for lettera, frequenza in frequenze.items():
    if lettera in vocali:
        c_vocali += frequenza
    else:
        c_consonanti += frequenza
        
if c_vocali > c_consonanti:
    print("Ci sono più vocali")
elif c_consonanti > c_vocali:
    print("Ci sono più consonanti")
else:
    print("C'è un numero uguale di vocali e di consonanti")
