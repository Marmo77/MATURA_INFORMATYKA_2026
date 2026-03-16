plik = open("slowa_przyklad.txt", "r")

for line in plik.readlines():
    line = line.strip()
    print(line)

# ZADANIE 3.1.
# znajdywanie: "k?t" ? => ? -> losowe

print("-----------------")

def znajdz_slowo(slowo):
    for znak in slowo:
        print(znak)

znajdz_slowo("brokat")