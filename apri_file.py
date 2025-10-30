

with open("lines.txt", 'r') as f:
    
    # contenuti del file -> una stringa
    contenuti = f.read()
    # contenuti del file -> lista di stringhe (per righe)
    contenuti = f.readlines()
    # contenuti del file -> iterati per righe
    for riga in f:
        # fai qualcosa
        pass # (pass non fa niente)
    