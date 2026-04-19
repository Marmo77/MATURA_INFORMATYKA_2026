
def Koduj(n):
    if n == 1:
        return ""
    else:
        k = n // 2
        if k % 2 == 0:
            return Koduj(k) + "A"
        else:
            return "B"+ Koduj(k)
# print(Koduj(1)) # ""
# print(Koduj(2)) # B
# print(Koduj(12)) # BBA""
# print(Koduj(33)) # BAAAA""
# print(Koduj(158)) # BBBBBAA""

# print(Koduj(1022))
#Zadanie 2.2.

# 12 Koduj(12) wywolania: 4
# 33 Koduj(33) wywolania: 6
# 1022 Koduj(1022) wywolania: 10

# Zadanie 2.3.
# sprawdzamy które 6 cyfrowe dadza taki sam wynik czyli zaczynamy

# od 100000 i dodajemy +1 i sprawdzamy czy są powtórki

ilosci = {}

print("-----------------")
for n in range(50,70):
    k = Koduj(n)
    print(n, k)
    if len(k) == 6:
        if k not in ilosci:
            ilosci[k] = 1
            print(n)
        else:
            ilosci[k] += 1
            print(f"POWTORKA dla {k}: {n}")
    else:
        pass

print(ilosci)
#67 dla BBAAAA
#68 dla BBAAAA
print("-----ilosci--------")

print(Koduj(67)) # odp : 67 i 68
print(Koduj(68))

print("----------------------")