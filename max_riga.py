max_len = -1
riga_lunga = ""

with open("lines.txt", "r") as file:

    for line in file:
        if len(line) > max_len:
            riga_lunga = line
            max_len = len(line)

print(f"La riga più lunga del file è:\n{riga_lunga.strip()}\nCon {max_len} caratteri.")
