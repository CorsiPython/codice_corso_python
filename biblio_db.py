import sqlite3 as sql
from dataclasses import dataclass

@dataclass
class PK:
    titolo: str
    autore: str
    anno: int

def cerca_libro(cursor, titolo):

    cursor.execute("""
                SELECT * 
                FROM libri
                WHERE libri.titolo = ?
                   """, (titolo,))
    return cursor.fetchall()


def cerca_per_autore(cursor, autore):

    cursor.execute(
        """
                SELECT * 
                FROM libri
                WHERE libri.autore = ?
                ORDER BY libri.anno DESC
                   """,
        (autore,),
    )
    return cursor.fetchall()

def presta_libro(cursor, key: PK):

    cursor.execute(
        """
        SELECT COUNT(*) FROM libri as l
        WHERE l.autore = ? 
        AND l.anno = ?
        AND l.titolo = ?
        """, (key.autore, key.anno, key.titolo)
    )

    if cursor.fetchone()[0]:
        print("Libro Trovato!")
        cursor.execute(
            """
        UPDATE libri as l SET disponibile = 0
        WHERE l.autore = ? 
        AND l.anno = ?
        AND l.titolo = ?
        """,
            (key.autore, key.anno, key.titolo),
        )
        return True

    return False


def restituisci_libro(cursor, key: PK):

    cursor.execute(
        """
        SELECT COUNT(*) FROM libri as l
        WHERE l.autore = ? 
        AND l.anno = ?
        AND l.titolo = ?
        """,
        (key.autore, key.anno, key.titolo),
    )

    if cursor.fetchone()[0]:
        print("Libro Trovato!")
        cursor.execute(
            """
        UPDATE libri as l SET disponibile = 1
        WHERE l.autore = ? 
        AND l.anno = ?
        AND l.titolo = ?
        """,
            (key.autore, key.anno, key.titolo),
        )
        return True

    return False


def libri_disponibili(cursor):
    
    cursor.execute("""
                   SELECT * FROM libri as l WHERE l.disponibile = 1
                   """)
    res = cursor.fetchall()
    
    return len(res), res


with sql.connect("biblioteca.db") as db:
    cursor = db.cursor()

    # MIGRATION

    cursor.execute("""CREATE TABLE IF NOT EXISTS libri (
        titolo TEXT,
        autore TEXT,
        anno INTEGER,
        disponibile INTEGER,
        PRIMARY KEY (titolo, autore, anno)
    )""")
    db.commit()

    books = [
        {"titolo": "Don Quixote", "autore": "Miguel de Cervantes", "anno": 1605, "disponibile": 1},
        {"titolo": "Paradise Lost", "autore": "John Milton", "anno": 1667, "disponibile": 1},
        {"titolo": "Gulliver's Travels", "autore": "Jonathan Swift", "anno": 1726, "disponibile": 1},
        {"titolo": "Robinson Crusoe", "autore": "Daniel Defoe", "anno": 1719, "disponibile": 1},
        {"titolo": "Pride and Prejudice", "autore": "Jane Austen", "anno": 1813, "disponibile": 1},
        {"titolo": "Jane Eyre", "autore": "Charlotte Brontë", "anno": 1847, "disponibile": 1},
        {"titolo": "Wuthering Heights", "autore": "Emily Brontë", "anno": 1847, "disponibile": 0},
        {"titolo": "Moby-Dick", "autore": "Herman Melville", "anno": 1851, "disponibile": 1},
        {"titolo": "Great Expectations", "autore": "Charles Dickens", "anno": 1861, "disponibile": 0},
        {"titolo": "Crime and Punishment", "autore": "Fyodor Dostoevsky", "anno": 1866, "disponibile": 1},
        {"titolo": "War and Peace", "autore": "Leo Tolstoy", "anno": 1869, "disponibile": 1},
        {"titolo": "Anna Karenina", "autore": "Leo Tolstoy", "anno": 1877, "disponibile": 0},
        {"titolo": "The Brothers Karamazov", "autore": "Fyodor Dostoevsky", "anno": 1880, "disponibile": 1},
        {"titolo": "Madame Bovary", "autore": "Gustave Flaubert", "anno": 1856, "disponibile": 1},
        {"titolo": "Les Misérables", "autore": "Victor Hugo", "anno": 1862, "disponibile": 0},
        {"titolo": "The Count of Monte Cristo", "autore": "Alexandre Dumas", "anno": 1844, "disponibile": 1},
        {"titolo": "A Tale of Two Cities", "autore": "Charles Dickens", "anno": 1859, "disponibile": 1},
        {"titolo": "Frankenstein", "autore": "Mary Shelley", "anno": 1818, "disponibile": 1},
        {"titolo": "Dracula", "autore": "Bram Stoker", "anno": 1897, "disponibile": 1},
        {"titolo": "The Odyssey", "autore": "Homer", "anno": -800, "disponibile": 1},
        {"titolo": "The Iliad", "autore": "Homer", "anno": -750, "disponibile": 0},
        {"titolo": "The Divine Comedy", "autore": "Dante Alighieri", "anno": 1320, "disponibile": 1},
        {"titolo": "Hamlet", "autore": "William Shakespeare", "anno": 1603, "disponibile": 1},
        {"titolo": "The Scarlet Letter", "autore": "Nathaniel Hawthorne", "anno": 1850, "disponibile": 1},
        {"titolo": "The Adventures of Huckleberry Finn", "autore": "Mark Twain", "anno": 1884, "disponibile": 0},
    ]

    for book in books:

        cursor.execute(
            """
            INSERT OR REPLACE INTO libri (titolo, autore, anno, disponibile)
            VALUES (?, ?, ?, ?)
            """, tuple(book.values())
        )

    print(cerca_libro(cursor, "Hamlet"))
    print(cerca_per_autore(cursor, "Homer"))
    print(
        presta_libro(
            cursor, PK("Hamlet", "William Shakespeare", 1603)
        )
    )
    
    n_libri, libri = libri_disponibili(cursor)
    print(f"Ci sono {n_libri} libri disponibili:\n{libri}")