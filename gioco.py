# Scrivi un programma che, con un ciclo while , chieda all'utente di indovinare un
# numero segreto (ad esempio 7). Il programma deve continuare a chiedere finché
# l'utente non indovina il numero, stampando un messaggio di congratulazioni alla fine.
import random 


numero_segreto = random.randint(0, 20)

while True:
    n = int(input("Indovina il numero: "))
    
    if n == numero_segreto:
        print("Congratulations!")
        break
    else:
        if n > numero_segreto:
            print("Troppo alto!")
        else:
            print("Troppo basso!")