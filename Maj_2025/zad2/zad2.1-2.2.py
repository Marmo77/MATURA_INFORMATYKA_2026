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

kwadraty = []
dlugosc_znakow_w_linii = 12
for i in range(0, len(wiersze) -2): 
    for j in range(0, dlugosc_znakow_w_linii -2):
        wiersz1 = wiersze[i]
        wiersz2 = wiersze[i+1]
        wiersz3 = wiersze[i+2]
        
        linia1 = wiersz1[j] + wiersz1[j+1] + wiersz1[j+2]
        linia2 = wiersz2[j] + wiersz2[j+1] + wiersz2[j+2]
        linia3 = wiersz3[j] + wiersz3[j+1] + wiersz3[j+2]
        
        
        czy_linie_idetyczne = (linia1[0] == linia1[1] == linia1[2])
        czy_kwadrat_identyczny = (linia1 == linia2 == linia3)
        
        if (czy_linie_idetyczne and czy_kwadrat_identyczny):
            # print("L. kwadraty: "+ len(kwadraty))
            kwadraty.append((i+2, j+2))
            
for wiersz, pozycja in kwadraty:
    print(len(kwadraty), wiersz, pozycja)