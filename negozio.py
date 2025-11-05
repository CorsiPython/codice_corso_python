from dataclasses import dataclass

class Prodotto:
    
    def __init__(self, nome: str, prezzo: float, giacenza: float):
        
        self.nome = nome
        self.prezzo = prezzo
        self.giacenza = giacenza
        
    def __str__(self):
        
        return f"""
            Il prodotto è {self.nome}
            Abbiamo {self.giacenza} unità
            Il prezzo di vendita è {self.prezzo} EUR
        """
        
@dataclass
class ProdottoDataclass:
    nome: str
    prezzo: float
    giacenza: float
    
    def __str__(self):
        
        return f"""
            Il prodotto è {self.nome}
            Abbiamo {self.giacenza} unità
            Il prezzo di vendita è {self.prezzo} EUR
        """
        
        
if __name__ == "__main__":
    
    detersivo = ProdottoDataclass("Dash", 6.50, 20)
    birra = ProdottoDataclass("Peroni", 1.50, 60)
    
    print(detersivo, birra)