from rettangolo import Rettangolo, Quadrato


rettangoli = [
    Rettangolo(4, 5),
    Rettangolo(6, 2),
    Rettangolo(10, 2),
    Quadrato(8)
]

for r in rettangoli:
    print(r)
    print(r.area())