frase = "Mi chiamo Dario"
k = 3

print("== CON IL WHILE ==")
i = 0
while i < k:
    print(frase)
    i += 1

print("== CON FOR E RANGE ==")
print(list(range(k)))
for i in range(k):
    print(frase)
