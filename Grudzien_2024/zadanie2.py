def F(x,p):
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x//p,p) + c
        else:
            return F(x//p,p) - c

# print(F(220,4))

for liczba in range(1,1000):
    p = 4
    wynik = F(liczba,p)
    if wynik == 0:
        print(f"MAM LICZBE: {liczba}")
print(F(16,3))
print("--------")

ilosc_powt = 0
liczba = 220
p = 4
while liczba > 0:
    liczba = liczba // p
    # print(liczba)
    ilosc_powt += 1

print("-------")
print(ilosc_powt+1)