class Coda:

    def __init__(self, coda=None):

        self.coda = coda if coda else []

    def push(self, x):
        self.coda.append(x)

    def pop(self):
        return self.coda.pop(0)

    def peek(self):
        return self.coda[0]

    def size(self):
        return len(self.coda)

    def is_empty(self):

        return len(self.coda) == 0

# Usa la classe Coda per implementare una funzione is_palindrome(s) che prende una
# stringa s e restituisce True se la stringa è un palindromo (si legge uguale da sinistra a
# destra e da destra a sinistra), altrimenti False .

def is_palindrome(s):
    coda = Coda()
    
    for c in s:
        coda.push(c)
        
    # "anna"
    # ["a", "n", "n", "a"]
    
    # iteriamo la stringa AL CONTRARIO
    for c in reversed(s):
        altro = coda.pop()
        if c != altro:
            return False
    return True


if __name__ == "__main__":

    coda = Coda([1, 2, 3, 4, 5, 6])

    print(coda.pop())
    print(coda.size())
    print(coda.peek())
    coda.push(11)

    for _ in range(coda.size()):
        print(coda.pop())

    print(coda.is_empty())
    
    stringa = "Sono al contrario"
    print(is_palindrome(stringa))
    print(is_palindrome("anna"))
