A = set([1, 2, 3, 4])
B = set([3, 4, 5, 6])

C = set()
for n in A:
    if n in B:
        C.add(n)

C = [n for n in A if n in B]
