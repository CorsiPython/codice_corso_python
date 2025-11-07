import sqlite3 as sql


with sql.connect("biblioteca.db") as db:
    cursor = db.cursor()
    
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
        try:
            cursor.execute(
                """
                INSERT INTO libri (titolo, autore, anno, disponibile)
                VALUES (?, ?, ?, ?)
                """, tuple(book.values())
            )
        except sql.IntegrityError as e:
            print(e)
            print(f"Hai provato a inserire un record doppio:\n{book}")