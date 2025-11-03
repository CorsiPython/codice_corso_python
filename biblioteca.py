from dataclasses import dataclass
import pickle
import os


@dataclass(order=True)
class Libro:

    titolo: str
    autore: str
    anno_pub: int

    def descrizione(self):

        return f"""
              Titolo: {self.titolo}
              Autore: {self.autore}
              Anno: {self.anno_pub}
              """


class Sezione:

    def __init__(self, tema, libri=None):

        self.tema = tema
        self.libri = libri if libri else []

    def aggiungi_libro(self, libro):

        self.libri.append(libro)

    def rimuovi_libro(self, titolo):

        for i, libro in enumerate(self.libri):

            if libro.titolo == titolo:
                self.libri.pop(i)
                break

    def stampa_libri(self):

        for libro in self.libri:
            print(libro.descrizione())

    def cerca_libro(self, titolo):

        for libro in self.libri:
            if libro.titolo == titolo:
                return libro
        return None

    def cerca_autore(self, autore):

        autori = []

        for libro in self.libri:
            if libro.autore == autore:
                autori.append(libro)

        return Sezione("Ricerca", autori)


class Biblioteca:

    def __init__(self, sezioni=None):

        self.sezioni = sezioni if sezioni else []

    def aggiungi_sez(self, sez):
        self.sezioni.append(sez)

    def rimuovi_sez(self, tema):

        self.sezioni = filter(lambda sez: sez.tema != tema, self.sezioni)

    def cerca_libro(self, titolo):

        for sez in self.sezioni:
            libro = sez.cerca_libro(titolo)
            if libro:
                return libro
        return None

    def cerca_autore(self, autore):

        autori = []

        for sez in self.sezioni:
            autori += sez.cerca_autore(autore).libri

        return Sezione("Ricerca", autori)

    def stampa_sezioni(self):
        for sez in self.sezioni:
            print(sez.tema)
            sez.stampa_libri()


if __name__ == "__main__":

    if not os.path.exists("biblio.pkl"):

        biblio = Biblioteca()

        # parti da qua quando esegui il file
        libri = [
            Libro("1984", "George Orwell", 1949),
            Libro("Animal Farm", "George Orwell", 1945),
        ]

        sez = Sezione("Romanzi", libri)

        sez.aggiungi_libro(Libro("Io, Robot", "Isaac Asimov", 1950))

        sez.stampa_libri()

        ret = sez.cerca_libro("Divina Commedia")
        if not ret:
            print("Libro not Found")
        else:
            print(f"Libro trovato:\n{ret.descrizione()}")

        trovato = sez.cerca_autore("George Orwell")
        trovato.stampa_libri()

        biblio.aggiungi_sez(sez)

        ## Creo Nuova Sezione

        libri = [
            Libro("Il Signore Degli Anelli", "J.R.R Tolkien", 1954),
            Libro("Lo Hobbit", "J.R.R Tolkien", 1937),
            Libro("Darkest Mind", "Alexandra Bracken", 2015),
        ]

        biblio.aggiungi_sez(Sezione("Fantasy", libri))
        print("##### BIBLIOTECA #####")
        biblio.stampa_sezioni()

        with open("biblio.pkl", "wb") as f:
            pickle.dump(biblio, f)
    else:
        with open("biblio.pkl", "rb") as f:
            biblio = pickle.load(f)
        biblio.stampa_sezioni()
