import math
plik = open("dron_przyklad.txt","r")


wewnatrz_kwadratu = []
tor_lotu = [(0,0)]
idx = 1
for line in plik.readlines():
    line = line.strip()

    A,B = line.split(" ")
    A,B = int(A),int(B)
    punkt = (A,B)
    if idx == 1:
        tor_lotu.append(punkt)
    else:
        X,Y = punkt
        stary_X,stary_Y = tor_lotu[idx-1]
        nowy_X,nowy_Y = X+stary_X,Y+stary_Y
        # print(nowy_X,nowy_Y)
        punkt = (nowy_X,nowy_Y)
        tor_lotu.append(punkt)

    idx += 1
# print(tor_lotu)

srodki_odcinkow = []
for punkt in tor_lotu:
    for kordynaty in tor_lotu:
        X,Y = punkt
        nowy_X,nowy_Y = kordynaty
        nowy_punkt = ((X+nowy_X)//2, (Y+nowy_Y)//2)
        print(nowy_punkt)
        srodki_odcinkow.append(nowy_punkt)

for punkt in srodki_odcinkow:
    if punkt in tor_lotu:
        print("JEA")
        print(punkt)


# podpunkt a)
for punkt in tor_lotu:
   if punkt[0] > 0 and punkt[1] > 0 and punkt[0] < 5000 and punkt[1] < 5000:
       wewnatrz_kwadratu.append(punkt)

print(wewnatrz_kwadratu)
ilosc_wewnatrz = len(wewnatrz_kwadratu)
print(ilosc_wewnatrz)
