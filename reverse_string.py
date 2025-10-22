# Scrivi un programma che chieda all'utente di inserire una stringa e stampi la stringa al
# contrario, utilizzando un ciclo for .
 
nome = "Luca mangia la mela"

lista = []
print(nome, len(nome))
for lettera in reversed(nome):
    lista.append(lettera)
    
print("".join(lista))