
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
ciekawe_nudne(4) # NIE
ciekawe_nudne(229) # NIE
ciekawe_nudne(82)   # TAK

print("--------------------------")

#1.2.