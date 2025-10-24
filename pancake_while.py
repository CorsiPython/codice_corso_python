

def bake_pancakes(latte, farina):
    
    pancakes = 0
    while latte >= 250 and farina >= 200:
        pancakes += 4
        latte -= 250
        farina -= 200
        
    return pancakes 


# === programma principale

milk = int(input("Inserisci il Latte: "))
flour = int(input("Inserisci la Farina: "))


pancake = bake_pancakes(milk, flour)
print(f"Possiamo cucinare {pancake} pancakes")