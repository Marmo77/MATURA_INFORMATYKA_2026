from enum import Flag

ciag = []

def ciekawe_nudne(n):
    n_str = str(n)
    kwadraty = []
    for i in range(len(n_str)):
        square = int(n_str[i]) ** 2
        kwadraty.append(square)
    print(kwadraty)
    suma = sum(kwadraty)
    print(suma)
    if suma != 1:
        ciekawe_nudne(suma)
    else:
        print("nudna")

#CZY NUDNA?
# ciekawe_nudne(4) # NIE
# ciekawe_nudne(229) # NIE
# ciekawe_nudne(82)   # TAK

print("--------------------------")

#1.2.

def SumaKwCyfr(n):
    n_copy = n
    suma = 0
    while n_copy > 0:
        ostatnia  = n_copy % 10
        # print(ostatnia)
        kw_ostatniej = ostatnia * ostatnia
        suma += kw_ostatniej
        n_copy = n_copy // 10
    return suma
print(SumaKwCyfr(123))

#1.3.
print("-------------------------")

def CzyNudna(n):
    odwiedzone = set()

    while n !=1 and n not in odwiedzone:
        odwiedzone.add(n)
        print(odwiedzone)
        n = SumaKwCyfr(n) # teraz sumujemy
    #jesli suma = 1 t
    if n == 1:
        return True
    else:
        return False

print(CzyNudna(13))