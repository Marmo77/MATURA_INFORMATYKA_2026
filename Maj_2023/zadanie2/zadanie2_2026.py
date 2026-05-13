
#Zadanie 2.1.
def na_binarna(n):
    binarna = 0
    potega = 1
    while n > 0:
        liczba = n % 2
        binarna += liczba * potega
        potega = potega * 10
        n = n // 2
    return binarna

def bloki_binarnej(n):
    binarna = na_binarna(n)
    b = 1
    while binarna > 9:
        ostatnia = binarna % 10
        przedostatnia = (binarna // 10) % 10 #usuwamy ostatnia i bierzemy z niej ostatnia czyli przedostania
        #jesli nastepny element jest inny
        #czyli obecna ostatnia jest rozna od kolejnej ostatniej to dodajemy bloki
        if ostatnia != przedostatnia:
            b += 1
        binarna = binarna // 10

    return b

print(bloki_binarnej(245))
print("-------------------")
#Zadanie 2.2 i 2.3.

def bloki_binarnejZad2(binarna):
    b = 1
    while binarna > 9:
        ostatnia = binarna % 10
        przedostatnia = (binarna // 10) % 10 #usuwamy ostatnia i bierzemy z niej ostatnia czyli przedostania
        #jesli nastepny element jest inny
        #czyli obecna ostatnia jest rozna od kolejnej ostatniej to dodajemy bloki
        if ostatnia != przedostatnia:
            b += 1
        binarna = binarna // 10
    return b


with open("bin.txt") as f:
    liczby = f.readlines()
    ilosc_blokow_wiekszych_mnr_2 = 0
    for binarna in liczby:
        binarna = binarna.strip()
        # print(binarna)
        ilosc_blokow = bloki_binarnejZad2(int(binarna))
        # print(ilosc_blokow)
        if ilosc_blokow <= 2:
            ilosc_blokow_wiekszych_mnr_2+=1
    print(ilosc_blokow_wiekszych_mnr_2) # 10

    print("---------")
    with open("bin.txt") as f:
        liczby = f.readlines()
        najwieksza_liczba = 0
        najwikesza_binarna = 0
        for binarna in liczby:
            binarna = binarna.strip()
            dziesietna = int(binarna,2)
            if najwieksza_liczba < dziesietna:
                najwieksza_liczba = dziesietna
                najwikesza_binarna = binarna
        print(najwikesza_binarna) #1110100011100011100

#Zadanie 2.5.
print("------")
with open("bin.txt") as f:
    liczby = f.readlines()

    for binarna in liczby:
        binarna = binarna.strip()

        def xorBinarnej(p):
            # p <= binarna

            dziesietna = int(binarna,2)
            # print(dziesietna)
            druga_binarna = bin(dziesietna // 2)[2:]

            while len(druga_binarna) != len(p):
                druga_binarna = "0" + druga_binarna
            # print(binarna)
            # print(druga_binarna)
            #XOR'owanie
            wynik_xor = ""
            for i in range(len(p)):
                potega = 1
                if p[i] != druga_binarna[i]:
                    wynik_xor += "1"
                elif p[i] == druga_binarna[i]:
                    wynik_xor += "0"
            # wynik_xor = int(wynik_xor, 2)
            # print(wynik_xor)
            return wynik_xor



        print(xorBinarnej(binarna))
        with open("wyniki2_5_X.txt", "a") as p:
            p.write(f"{str(xorBinarnej(binarna))}\n")