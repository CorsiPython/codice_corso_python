# Scrivi un programma che, con un ciclio while , chiede all utente di inserire una serie di
# parole, finché non viene inserita la parola "stop". Alla fine, stampa tutte le parole
# inserite concatenate in una singola stringa, separate da uno spazio.

parole = []

while True:
    word = input("Inserisci una parola: ")
    if word == "stop":
        break
    parole.append(word)

print(parole)
frase = " ".join(parole)
print(frase)
