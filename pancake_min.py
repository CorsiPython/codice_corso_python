

def bake_pancakes(latte, farina):
    
    pancakes_milk = latte // 250
    pancakes_flour = farina // 200
        
    return min(pancakes_milk, pancakes_flour) * 4


# === programma principale

milk = int(input("Inserisci il Latte: "))
flour = int(input("Inserisci la Farina: "))


pancake = bake_pancakes(milk, flour)
print(f"Possiamo cucinare {pancake} pancakes")