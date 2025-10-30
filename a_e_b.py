# A & B

# Scrivi un programma che chiede all'utente di inserire una stringa di A e B (controlla che
# l'input sia valido), dopodichè, dato un numero x = len(stringa) // 2 , leggi la stringa e,
# ogni volta che incontri due caratteri uguali consecutivi (AA o BB), sostituiscili con un
# singolo carattere (A o B).
# Per ogni sostituzione, se il carattere uguale era A, x = (x * 3) + 2 , se era B, x = (x // 2) -
# 1 .
#
# Stampa la stringa risultante e il valore di x.

comando = input("Inserisci una stringa di A e di B: ")

for c in comando:
    if c not in "AB":
        raise ValueError("Comando Invalido!")

lista_comandi = [c for c in comando]
print(lista_comandi)

x = len(comando) // 2

has_changed = False
while True:
    for i in range(len(lista_comandi) - 1):
        
        comando = lista_comandi[i]
        
        if comando == lista_comandi[i+1]:
            ## unione
            lista_comandi.pop(i)
            has_changed = True
            break
    
    if not has_changed:
        break
    has_changed = False
    
print(f"Il numero finale è: {x}")
print(f"Il comando finale è {"".join(lista_comandi)}")