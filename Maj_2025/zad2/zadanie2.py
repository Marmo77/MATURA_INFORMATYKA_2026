#-------------------

# Połączenie zadań i zapis do pliku wynik2.txt


#-------------------

# palindromy
# 2.1 
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
            
wynik.write("2.2.\n")
for wiersz, pozycja in kwadraty:
    print(len(kwadraty), wiersz, pozycja)
    wynik.write(f"{len(kwadraty)} {wiersz} {pozycja}\n")


#2.3 

plik = open("symbole.txt", "r")
# o = 0
# + = 1
# * = 2

najwyzszy_wynik = -1
najwyzszy_wynik_text = ""
wiersze = plik.readlines()

for wiersz in wiersze:
    aktualny_wynik = ""
    wiersz = wiersz.strip()
    
    for znak in wiersz:
        if znak == "o":
            aktualny_wynik += "0"
        elif znak == "+":
            aktualny_wynik += "1"
        elif znak == "*":
            aktualny_wynik += "2"
    #konwersja na dziesietny
    
    odwrocony_wynik = aktualny_wynik[::-1] #odwrocenie aby isc od tylu
    wynik_dziesietny = 0
    for idx,liczba in enumerate(odwrocony_wynik): # dla kazdej liczby mnozyzymy ja razy 3 do potęgi takiej na jakim są indeksie
        # print(idx,liczba)
        wynik_dziesietny += int(liczba) * 3**idx
        
    
    if wynik_dziesietny > najwyzszy_wynik:
        najwyzszy_wynik = wynik_dziesietny
        najwyzszy_wynik_text = wiersz

print(f"{najwyzszy_wynik} {najwyzszy_wynik_text}")
wynik.write(f"2.3.\n")
wynik.write(f"{najwyzszy_wynik} {najwyzszy_wynik_text}\n")

# 2.4

suma_wynikow_pliku = 0
suma_wynikow_pliku_text = ""

for wiersz in wiersze:
    aktualny_wynik = ""
    wiersz = wiersz.strip()
    
    for znak in wiersz:
        if znak == "o":
            aktualny_wynik += "0"
        elif znak == "+":
            aktualny_wynik += "1"
        elif znak == "*":
            aktualny_wynik += "2"
            
    # konwersja na dziesietny z trojkowego, poprzez int
    
    wynik_dziesietny = int(aktualny_wynik,3)
    suma_wynikow_pliku += wynik_dziesietny # dla kazdego wiersza obliczamy ile wynosi wynik dziesietny i go dodajemy do wyniku calego pliku
    

#trzeba teraz sume dziesietna przekontwertowac na trojkowy
trojkowy_suma = ""
s = suma_wynikow_pliku
while s > 0:
    trojkowy_suma = str(s%3) + trojkowy_suma # dodawanie do przodu zamist dodac na koniec np. 0 na koniec 10 to dodajemy do przodu 01
    s = s //3 # div mod
    
# print(trojkowy_suma)

# teraz trojkowy na symbole
s_text = suma_wynikow_pliku_text 
for liczba in trojkowy_suma:
    if liczba == "0":
        s_text += "o"
    elif liczba == "1":
        s_text += "+"
    elif liczba == "2":
        s_text += "*"

print(suma_wynikow_pliku, s_text)

wynik.write("2.4.\n")
wynik.write(f"{suma_wynikow_pliku} {s_text}")


#zmienna wynik zapisuje do pliku wynik2.txt wyniki poprzedzone numerem zadania