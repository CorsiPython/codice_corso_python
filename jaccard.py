A = set([1, 2, 3, 4])
B = set([3, 4, 5, 6])

C_intersection = set()
for n in A:
    if n in B:
        C_intersection.add(n)


C_union = set()
for a in A:
    C_union.add(a)
for b in B:
    C_union.add(b)

jaccard = len(C_intersection) / len(C_union)

print(f"J(A,B) = {jaccard}")
