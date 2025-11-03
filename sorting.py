# Senza usare .sort() , sorted() o altre funzioni di ordinamento predefinite,
# scrivi un programma che ordini una lista di numeri in ordine crescente
# Suggerimento: puoi implementare un algoritmo di ordinamento semplice come il
# bubble sort, selection sort o insertion sort.

import random

numeri = [random.randint(0, 1000) for _ in range(10)]


def ordina_ins(lista):

    lista = [x for x in lista]
    # Insertion Sort
    for i in range(len(lista)):
        minimum = float("inf")
        pos_min = 0
        for j in range(i, len(lista)):
            if lista[j] < minimum:
                minimum = lista[j]
                pos_min = j
        # ho trovato il minimo
        lista[i], lista[pos_min] = lista[pos_min], lista[i]
    return lista


def ordina_bubb(lista):

    lista = [x for x in lista]

    while True:
        changed = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                changed = True

        if not changed:
            break

    return lista


print(numeri)
print(ordina_ins(numeri))
print(ordina_bubb(numeri))
