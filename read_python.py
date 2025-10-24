# Dato il file lines.txt , scrivi un programma che 
# legge il file e crea una nuova lista
# contenente solo le righe che contengono la parola "Python" 
# (ignorando maiuscole/minuscole). Stampa la lista risultante.


with open('lines.txt', 'r') as file:
    righe_python = []
    
    for line in file:
        if "Python" in line:
            righe_python.append(line)
            
print(f"Le righe con python sono:\n{righe_python}")