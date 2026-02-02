#3.1
# NWD
import math
plik = open("dron_przyklad.txt", "r")
wiersze = plik.readlines()

licznik_nwd = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    
    A = abs(int(wiersz.split(" ")[0])) # abs = bezwzgledna
    # if A < 0: A = A * -1  -> inny sposob na absolutna
    B = abs(int(wiersz.split(" ")[1]))
    print(A,B)
    
    nwd = math.gcd(A,B)
    if nwd > 1:
        licznik_nwd += 1

print(licznik_nwd)


# def NWD(A, B):
#     if A < 0:
#         A = A * -1 
#     if B < 0:
#         B = B * -1
#     print(A,B)

#3.2
print("---\n3.2")
# a)

x = 0 #startowe
y = 0 #startowe

naleza_wewnatrz = 0

for wiersz in wiersze:
    wiersz = wiersz.strip().split(" ")
    dx = int(wiersz[0])
    dy = int(wiersz[1])
    x = x + dx
    y = y + dy
    
    if x > 0 and x < 5000 and y > 0 and y < 5000:
        naleza_wewnatrz +=1
        
print(naleza_wewnatrz)


x,y = 0, 0

punkty = []
punkty.append((x,y))

for wiersz in wiersze:
    wiersz = wiersz.strip().split(" ")
    dx = int(wiersz[0])
    dy = int(wiersz[1])
    x = x + dx
    y = y + dy
    
    punkty.append((x,y))
    
print(punkty)

# punkt[0] i punkt[1] (0,0) i (2000,1001) - wyliczamy srednia i sprawdzamy czy ten punkt znajduje sie w naszych punktach

for i in range(len(punkty)): # przez wszystkie punkty
    for j in range(i+1, len(punkty)):
        x1, y1 = punkty[i]
        x2, y2 = punkty[j]
        # print(x1,y1,x2,y2)
        
        # tylko jesli suma x1 i x2 jest parzysta to wyjdzie wynik bo inaczej np .5 po przecinku i wtedy nie moze byc tak samo z y'kami
        
        if ((x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0):
            sx = (x1 + x2) // 2 #srodek x
            sy = (y1 + y2) // 2 #srodek y
            srodkowy_punkt = (sx,sy)
            # print(srodkowy_punkt)
            # dla kazdego punktu w punkty sprawdzamy czy srodkowe punkty pasuja do ktorgos z punktow
            for punkt in punkty:
                xp, yp = punkt
                if(xp == sx and yp == sy): # jesli tak to wypisujemy srodkowe punkty
                    print(f"({x1}, {y1}), ({sx}, {sy}), ({x2}, {y2})") # x1,y1 -> poczatkowy punkt x2,y2 -> koncowy punkt sx,sy -> srodkowy punkt
                    
                    
