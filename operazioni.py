def calculate(a, op, b):

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("operands must be integers")

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op in ("/", "//"):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a // b
    elif op == "*":
        return a * b
    elif op == "%":
        if b == 0:
            raise ZeroDivisionError("modulo by zero")
        return a % b
    else:
        raise ValueError(f"unknown operator: {op}")


with open("operazioni.txt", "r") as file:
    for i, riga in enumerate(file):
        operazione, risultato = riga.split("=")
        operazione = operazione.strip()
        risultato = int(risultato.strip())

        a, op, b = operazione.split(" ")

        res = calculate(a, op, b)
        if res != risultato:
            raise ValueError(
                f"C'è stato un errore a riga {i+1}: {riga.strip()}, Abbiamo invece calcolato {res}"
            )

    print("Tutte le operazioni erano calcolate in maniera corretta")
