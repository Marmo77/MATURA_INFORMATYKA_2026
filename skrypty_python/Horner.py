



# do odwracania liczb wykorzystujac pseudo kod lub kod bez funkcji pythona
def odwrocona_liczba(n): # n -> nasza liczba np. 32145 zamienia się na 54123
    odwrocna = 0

    while n > 0:
        ostatnia = n % 10 # ostatnia liczba np. z liczby 32145 jest 5 (w pierwszym przejsciu
        print(ostatnia)
        odwrocna = odwrocna * 10 + ostatnia # bierzemy naszą liczbe i np. dla 2 przejscia czyli liczba 4 bierzemy:
        # poprzednie 5 i mamy odwrocna = 5 * 10 + 4 => 54, pozniej dla 1 - odwrocona = 54 * 10 + 1 => 541
        n = n // 10 # skracamy o ostani element, czyli co przejscie odejmujemy ostatnią
    return odwrocna

print(odwrocona_liczba(32145))