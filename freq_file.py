# Dato il file lines.txt , scrivi un programma che 
# legge il file e calcola la frequenza di ogni
# lettera (da 'a' a 'z', ignorando maiuscole/minuscole) 
# usando un dizionario. Stampa il
# dizionario risultante.

def count_words(string):
    
    counts = {}
    
    for lettera in string:
        counts[lettera] = counts.get(lettera, 0) + 1
        
    return counts

with open("lines.txt", 'r') as file:
    content = file.read()
    
    diz = count_words(content)
    
print(f"Ecco il dizionario con le frequenze:\n{diz}")