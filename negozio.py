from dataclasses import dataclass
from typing import Optional


@dataclass
class Prodotto:
    nome: str
    prezzo: float
    giacenza: float

    def __str__(self):

        return f"""
    Il prodotto è {self.nome}
    Abbiamo {self.giacenza} unità
    Il prezzo di vendita è {self.prezzo}€
        """

    def vendi(self, quantita: float) -> float:

        if self.giacenza < quantita:

            raise ValueError(
                f"Prodotto non disponibile, hai chiesto {quantita}, ne abbiamo solo {self.giacenza}"
            )

        self.giacenza -= quantita
        return self.prezzo * quantita

    def rifornisci(self, quantita: float):

        print(f"Rifornito da {self.giacenza} a {self.giacenza + quantita}")
        self.giacenza += quantita


class Negozio:

    def __init__(self, prodotti=None):

        self.prodotti = [] if not prodotti else prodotti

    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.prodotti.append(prodotto)

    def visualizza_prodotti(self):

        print("Prodotti:")

        for prodotto in self.prodotti:
            print(prodotto)

    def cerca_prodotto(self, nome) -> Optional[Prodotto]:

        for prodotto in self.prodotti:
            if nome.lower() in prodotto.nome.lower():
                return prodotto
        return None

    def valore_inventario(self) -> float:

        valore = 0
        for prod in self.prodotti:
            valore += prod.giacenza * prod.prezzo

        return valore


class Carrello:

    def __init__(self, prodotti=None):
        self.prodotti = [] if not prodotti else prodotti

    def aggiungi(self, prodotto: Prodotto):
        self.prodotti.append(prodotto)

    def rimuovi(self, prodotto: Prodotto):

        self.prodotti = filter(lambda prod: prod.nome != prodotto.nome, self.prodotti)

    def totale(self) -> float:
        valore = 0
        for prod in self.prodotti:
            valore += prod.prezzo * prod.giacenza
        return valore


if __name__ == "__main__":

    detersivo = Prodotto("Dash", 6.50, 20)
    birra = Prodotto("Peroni", 1.50, 60)

    print(detersivo, birra)

    print("Vendo tre birre")
    birra.rifornisci(30)
    print(f"Costo: {birra.vendi(3)}")

    negozio = Negozio([detersivo, birra])
    negozio.visualizza_prodotti()

    print(f"L'inventario vale: {negozio.valore_inventario()}€")

    print("=== ACQUISTI ===")
    carrello = Carrello()
    while True:
        prod = input("Dimmi un prodotto che vuoi (stop per fermarti): ")
        if prod == "stop":
            break
        quantita = int(input("Se c'è, quanto ne vuoi? "))
        trovato = negozio.cerca_prodotto(prod)

        if trovato:

            try:
                _ = trovato.vendi(quantita)
            except ValueError as e:
                print(e)
                continue

            comprato = Prodotto(trovato.nome, trovato.prezzo, quantita)

            print("Prodotto aggiunto al carello")
            carrello.aggiungi(comprato)
        else:
            print(f"{prod} non è disponibile")

    prezzo_finale = carrello.totale()
    print(f"Hai pagato {prezzo_finale}€")

    print(negozio.valore_inventario())
