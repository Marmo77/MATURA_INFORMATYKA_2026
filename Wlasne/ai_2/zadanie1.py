#Zadanie 1.1.

#anagramy tyle samo liter Jeden wyraz co 2

# pomysł:
# dict który zbiera ilość liter i sprawdza czy są takie same

def sprawdz_anagramy(plik):
    anagramy = 0
    with open(plik, "r") as f:
        for line in f.readlines():
            line = line.strip()
            # print(line)
            tekst1, tekst2 = line.split(" ")

            # dla pierwszego tekstu :
            tekst1_dict = {}
            for litera in tekst1:
                if litera not in tekst1_dict:
                    tekst1_dict[litera] = 1
                else:
                    tekst1_dict[litera] += 1
            # dla drugiego tekstu
            tekst2_dict = {}
            for litera in tekst2:
                if litera not in tekst2_dict:
                    tekst2_dict[litera] = 1
                else:
                    tekst2_dict[litera] += 1

            # print(f"Liczba literek tekst 1: {tekst1_dict}")
            # print(f"Liczba literek tekst 2: {tekst2_dict}")
            #jeśli są anagramami:
            if tekst1_dict == tekst2_dict and tekst1 != tekst2: #prewencja - gdy tekst1 jest równy tekst2 (powtorzone slowo) KOT KOT <-
                anagramy +=1

    return anagramy

print(f"Anagramy: {sprawdz_anagramy("napisy.txt")}")

#1.2.

with open("napisy.txt", "r") as f:
    licznik = 0
    for line in f.readlines():
        line = line.strip()
        # print(line)
        tekst1, tekst2 = line.split(" ")

        # dla pierwszego tekstu :
        krotsze, dluzsze = sorted([tekst1,tekst2], key=len)

        if krotsze in dluzsze:
            licznik += 1
print(f"Zawiera się w słowie: {licznik}")


#1.3.

with open("napisy.txt", "r") as f:
    hasla = {}
    licznik = 0
    for line in f.readlines():
        line = line.strip()
        # print(line)
        tekst1, tekst2 = line.split(" ")

        # dla pierwszego tekstu :
        krotsze, dluzsze = sorted([tekst1,tekst2], key=len)

        haslo = ""
        for idx,litera in enumerate(krotsze):
            haslo += litera
            haslo += dluzsze[idx]

        #jednak odrzucamy to to poprostu nie istnieje ---
        # if len(dluzsze) > len(krotsze):
        #     pozostalosc = len(dluzsze) - len(krotsze)
        #     # print(pozostalosc)
        #     pozostale_slowo = dluzsze[pozostalosc:]
        #     haslo += pozostale_slowo
        # ---
        # print(haslo)
        suma_ascii = 0
        for l in haslo:
            ascii_kod = ord(l)
            suma_ascii += ascii_kod
        hasla[haslo] = suma_ascii
    # print(hasla)
    najwieksza = max(hasla, key=hasla.get)
    print(f"Hasło z najw. sumą ASCII: {najwieksza} - {hasla.get(najwieksza)}")