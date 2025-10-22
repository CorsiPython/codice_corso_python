frase = "Luca mangia la mela"
start = 1
end = 13

# soluzione 1
for i, lettera in enumerate(frase):
    if i >= start and i <= end:
        print(lettera, end="")
print()

# soluzione 2
for i in range(start, end+1):
    print(frase[i], end="")
print()

# soluzione 3
# GLI SLICE (in italiano le "fette")
print(frase[start : end + 1])