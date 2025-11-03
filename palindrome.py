# Scrivi `is_palindrome`, una funzione che dice se un nome è palindromo o no
# I nomi palindromi si leggono allo stesso modo sia da sinistra a destra che da destra a sinistra


def is_palindrome(parola):
    # Diversi modi per risolvere il problema!

    # 1) Usare funzioni built in di python

    # 2) Soluzione passo-passo
    for i, lettera in enumerate(parola):
        print(i, lettera)
        if lettera != parola[len(parola) - i - 1]:
            return False

    return True


nomi = ["anna", "andrea", "marco"]

print(nomi)
print(nomi[::-1])

print(list(filter(lambda x: is_palindrome(x), nomi)))
