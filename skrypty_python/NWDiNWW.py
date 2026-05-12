import math

liczba1 = 4
liczba2 = 180

nwd = math.gcd(liczba1,liczba2) # najwiekszy wspolny dzielnik (greatest common divisor)
print(nwd)

lcm = math.lcm(liczba1,liczba2) # najmniejsza wspólna wielokrotność (least common multiple)
print(lcm)

# ręcznie zrobione jako funkcja

#NWD
def nwd_f(a,b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
#NWW
def nww_f(a,b):
    return abs(a*b) // nwd_f(a,b)
print("-------")
print(nwd_f(liczba1,liczba2))
print(nww_f(liczba1,liczba2))