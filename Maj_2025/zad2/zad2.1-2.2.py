# palindromy
plik = open("symbole.txt", "r")

wiersze = plik.readlines()

for wiersz in wiersze:
    napis =  wiersz.strip()
    
    odwrocony = ""
    #odwracamy napis
    for i in range(len(napis), 0, -1):
        odwrocony += napis[i-1]
    
    #jesli jest palindromem - normalny == odwrocony
    if napis == odwrocony:
        print(napis)