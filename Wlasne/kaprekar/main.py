#
#
# k:int = 123456
#
# def dzielenie_calkowietej_parz_na_pol(k):
#     ilosc_liczb = 0
#     k_dla_ilosci_l = k
#
#     while k_dla_ilosci_l > 0: # przechodzi przez kazdy element dlugosci liczby 123456
#         ilosc_liczb += 1 # dodajemy 1 do dlugsoci
#
#         k_dla_ilosci_l //= 10 # skracamy dlugosc o statnia liczbe
#
#     # print(ilosc_liczb)
#
#     polowa_liczby = ilosc_liczb // 2
#     # print(polowa_liczby)
#     #teraz w pętli przechodzimy przez ostatnie 3 elementy i przypisujemy do wartosci b, a to co zostaje ustawiamy jako a
#
#     k_ab = k
#     # print(10**polowa_liczby)
#     b = 0
#     mnoznik_b = 1
#     licznik = 0
#     while licznik < polowa_liczby: #czyli jesli wieksze od polowy np. 123456 -> 6 dlugosc -> polowa: 3 -> 10**3 = 1000 czyli przejdzie 3 razy przez ostatni element
#         ostatnia = k_ab % 10 #ostatnia liczba z k
#
#         #dopisujemy ją do b
#         b += ostatnia * mnoznik_b
#         # print(b)
#         mnoznik_b *= 10 #co przejscie zwiększamy mnożnik o 10, czyli dla 543., bierzemy od tyłu - dla 3*1 = 3, pozniej 4*10 = 40, 5 * 100 = 500 => 500 + 40 + 3 => 543
#
#         k_ab //= 10 # ucinamy
#         licznik += 1
#
#      #k_ab jest tym co zostało z przerzucenia połowy do b
#     return k_ab, b
#
# a,b = dzielenie_calkowietej_parz_na_pol(k)
#
# print(a)
# print(b)


# n = int >= 10

#ZADANIE 2.3.

# n = 2757

def sprawdz_stopien_kaprekara(n: int):
    stopien_kaprekara = 0
    n_pot = n**2
    n_pot_str = str(n_pot)

    n_pot_str_l = len(str(n_pot))


    l, p = n_pot_str_l-1, -1 # l po lewej stronie wszystkie oprocz ostatniego, prawy: ostatni element i zwiekszamy o 1 co petle
    for i in range(n_pot_str_l-1):
        # print(n_pot_str[:l], n_pot_str[p:])
        a = int(n_pot_str[:l])
        b = int(n_pot_str[p:])
        # print(a, b)

        #sprawdzenie czy stopien_kaprekara ?
        if (a + b) <= n:
            stopien_kaprekara += 1

        # przesuwamy po sprawdzeniu l w prawo o 1, a p o jedno w lewo
        l -= 1
        p -= 1
    return stopien_kaprekara

plik = open("liczby2.txt", "r")

liczby = [] # [liczba, stopien]
for line in plik:
    line = line.strip()
    n = int(line)
    # print(f"Dla {n}, stopien: {sprawdz_stopien_kaprekara(n)}")
    liczby.append([n,sprawdz_stopien_kaprekara(n)])

# print(liczby)
najwiekszy_stopien = 0
najwieksza_liczba = 0
for liczba, stopien_k in liczby:
    if stopien_k > najwiekszy_stopien:
        najwiekszy_stopien = stopien_k
        najwieksza_liczba = liczba
print(f"Najwyższa liczba: {najwieksza_liczba} i jej stopień Kaprekara: {najwiekszy_stopien}")

#odp:
# Najwyższa liczba: 7746 i jej stopień Kaprekara: 4

