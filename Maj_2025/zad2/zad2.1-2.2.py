# palindromy
plik = open("symbole.txt", "r")

wiersze = plik.readlines()
odp21 = []

for wiersz in wiersze:
    napis =  wiersz.strip()
    
    odwrocony = ""
    #odwracamy napis
    for i in range(len(napis), 0, -1):
        odwrocony += napis[i-1]
    
    #jesli jest palindromem - normalny == odwrocony
    if napis == odwrocony:
        print(napis)
        odp21.append(napis)
        
wynik = open("wynik2.txt", "w")
wynik.write(f"2.1.\n")
for wyn in odp21:
    wynik.write(f"{wyn}\n")

print("------------")

# 2.2

