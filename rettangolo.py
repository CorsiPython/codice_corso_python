class Rettangolo:
    
    def __init__(self, base, altezza):
        # Costruttore 
        
        self.base = base
        self.altezza = altezza
        
        
    def area(self):
        
        return self.base * self.altezza
    
    def __str__(self):
        
        return f"Rettangolo(base={self.base}, altezza={self.altezza})"

class Quadrato(Rettangolo):

    def __init__(self, lato):
        super().__init__(lato, lato)
        

    def area(self):

        return super().area()

    def __str__(self):

        return f"Quadrato(lato={self.base})"
