lista = [1, 2, 3, 4, 5, 6, 7]
insieme = set([1, 2, 3])

lista_nuova = []

for n in lista:
    if n in insieme:
        continue
    lista_nuova.append(n)

print(lista_nuova)


## Usando Filter e Map

print(list(filter(lambda x: x not in insieme, lista)))
