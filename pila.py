class Pila:

    def __init__(self, pila=None):

        self.pila = pila if pila else []

    def push(self, x):
        self.pila.append(x)

    def pop(self):
        return self.pila.pop()

    def peek(self):
        return self.pila[-1]

    def size(self):
        return len(self.pila)

    def is_empty(self):

        return len(self.pila) == 0


def is_palindrome(s):
    pila = Pila()

    for c in s:
        pila.push(c)

    # "ciao"
    # ["o", "i", "a", "c"]

    # iteriamo la stringa AL CONTRARIO
    for c in s:
        altro = pila.pop()
        if c != altro:
            return False
    return True


if __name__ == "__main__":

    pila = Pila([1, 2, 3])

    print(pila.pop())
    print(pila.size())
    print(pila.peek())
    pila.push(11)

    for _ in range(pila.size()):
        print(pila.pop())

    print(pila.is_empty())

    ## La pila è vuota
    ## usiamola per invertire una stringa

    pila = Pila()

    stringa = "Sono al contrario"

    for c in stringa:
        pila.push(c)

    stringa = "".join([pila.pop() for _ in range(pila.size())])
    print(stringa)
    print(is_palindrome(stringa))
    print(is_palindrome("anna"))
