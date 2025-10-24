A = set([1,2,3,4])
B = set([3,4,5,6])

C = set()
for a in A:
    C.add(a)
for b in B:
    C.add(b)
    
print(C)