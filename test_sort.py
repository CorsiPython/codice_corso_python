from sorting import ordina_ins, ordina_bubb
import random

### TESTS ###


def test_ins():

    numeri = [random.randint(0, 1000) for _ in range(10)]
    assert sorted(numeri) == ordina_ins(numeri)


def test_bubble():

    numeri = [random.randint(0, 1000) for _ in range(10)]
    assert sorted(numeri) == ordina_bubb(numeri)
