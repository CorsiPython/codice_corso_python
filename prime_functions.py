import math

# funzione che dice "True" se è primo, "False" se non è primo
def is_prime(x):
    for n in range(2, int(math.sqrt(x))):
        if x % n == 0:
            return False
    return True