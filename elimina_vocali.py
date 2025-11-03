# Dato il file lines.txt , scrivi un programma che legge il file e crea un nuovo file chiamato
# no_vowels.txt in cui tutte le vocali (a, e, i, o, u, sia maiuscole che minuscole) sono state
# rimosse da ogni riga.


def filtra_lista(contenuto):

    filtrato = [lettera for lettera in contenuto if lettera.lower() not in "aeiou"]
    return "".join(filtrato)


def filtra_lista_for(contenuto):

    filtrato = []
    for lettera in contenuto:
        if lettera.lower() not in "aeiou":
            filtrato.append(lettera)

    return "".join(filtrato)


def filtra_mapfilter(contenuto):

    return "".join(
        list(filter(lambda lettera: lettera.lower() not in "aeiou", contenuto))
    )


with open("lines.txt", "r") as file:
    content = file.read()

contenuto_filtrato = filtra_mapfilter(content)

with open("no_vowels.txt", "w") as f:
    f.write(contenuto_filtrato)
