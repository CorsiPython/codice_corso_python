# Scrivi un programma che, data una stringa dall utente, crei la versione palindroma
# E.g.: "ciao" -> "ciaooaic"

nome = input("Inserisci la parola da palindromizzare: ")

pal = nome + nome[::-1]

print(pal)
