import math
plik = open("dron.txt","r")

nwd_wieksze_od_1 = 0
for line in plik.readlines():
    line = line.strip()

    A,B = line.split(" ")
    A,B = int(A),int(B)
    NWD = math.gcd(abs(A),abs(B))
    if NWD > 1:
        nwd_wieksze_od_1 += 1
print(nwd_wieksze_od_1)