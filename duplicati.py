# Scrivi una funzione che prende una lista di numeri e
# restituisce una nuova lista con i
# duplicati rimossi, mantenendo l'ordine originale degli elementi.

numeri = [1,2,1,3,2,1,2,3,2,2,2,1]
# unici = []
# conto = {}
# 
# for n in numeri:
#     conto[n] = conto.get(n, 0) + 1
#     if conto[n] == 1:
#         unici.append(n)
# 
# print(unici)
# print(conto)

insieme = set(numeri)
unici = list(insieme)
print(insieme)
print(unici)