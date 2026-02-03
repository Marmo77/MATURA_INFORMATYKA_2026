masa_ladunku = 0

plik = open("martianeum.txt", "r")

wiersze = plik.readlines()
wiersze.pop(0) # usuwa nagłowki (data	nazwa_obszaru	masa [kg]	zawartosc [%])

# 6.1

i = 0
# co potrzebujemy? - wziasc mase i % zawartosci i obliczyć ile zawartosci i dodac do sumy lacznej

masa_laczna_ladunku = 0
masa_laczna_martianeum = 0
for wiersz in wiersze:
    # if i < 20:
    wiersz = wiersz.strip()
    podzial = wiersz.split("	")
    masa_str = podzial[2]
    zawartosc_str = podzial[3]
    
    masa = ""
    #podmiana , na .
    for l in masa_str:
        if l == ",":
            masa += "."
        else:
            masa += l
    # print(masa)
    zawartosc = ""
    for l in zawartosc_str:
        if l == ",":
            zawartosc += "."
        else:
            zawartosc += l
    
    zawartosc = float(zawartosc)
    if zawartosc >= 1.0:
        martianeum_w_ladunku = float(masa) * zawartosc
    else:
        martianeum_w_ladunku = 0
    # print(masa, zawartosc)
    # print(f"Mart: {martianeum_w_ladunku}")
    masa_laczna_ladunku += float(masa)
    masa_laczna_martianeum += martianeum_w_ladunku
        # i += 1
    # else:
        # break
    
print(f"Masa ladunku calkowita: {round(masa_laczna_ladunku,1)}")
print(f"Masa laczna Martianeum: {round(masa_laczna_martianeum, 1)}")
