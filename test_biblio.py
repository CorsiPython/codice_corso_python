from biblioteca import Libro, Biblioteca, Sezione


def test_aggiungi_libro():

    biblio = Biblioteca([Sezione("Romanzi", [])])

    biblio.sezioni[0].aggiungi_libro(Libro("1984", "George Orwell", 1949))
    assert biblio.cerca_libro("1984")
