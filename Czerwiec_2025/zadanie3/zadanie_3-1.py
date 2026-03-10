# ciag: str = "356xv@@4vdfvdfD#$%@@#245"

liczby: list[int] = []
plik = open("dane.txt", "r")
for ciag in plik.readlines():
    ciag = ciag.strip()

    aktualna_liczba = ""
    for idx, znak in enumerate(ciag):
        if znak.isdigit(): #jesli jest int
            aktualna_liczba += znak
            # print(aktualna_liczba)
        else:
            if aktualna_liczba != "": # jesli nie jest pusty (czyli ma 1 lub wiecej)
                liczby.append(int(aktualna_liczba))
                aktualna_liczba = ""

        #dla ostatniej liczby która zamyka pętle (jesli jest taki przypadek
        if idx == (len(ciag)- 1):
            if aktualna_liczba.isdigit():
                liczby.append(int(aktualna_liczba))


    # print(liczby)

liczby_start_str_50 = 0
for liczba in liczby:
    liczba_str = str(liczba)
    # print(liczba_str)
    if liczba_str.startswith("50"):
        liczby_start_str_50 += 1
print(f"Zaczynają się od 50 początek: {liczby_start_str_50}")

with open("wyniki3_1.txt", "w") as f:
    f.write(f"Wynik dla 3.1:\n{liczby_start_str_50}")


# --------------------- ZADANIE 3.1.