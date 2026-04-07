# ZADANIE 1.2. - pseudo kod lub tylko liczby całkowite
# + - * / // % > < >= <= == =

# najbardziej znacząca cyfra => czyli dla np. 254 to jest 2 bo 2.. -> 200
# czyli najwiecej value i jest  9 > n > 0

# cyfrowe dopełnienie liczby


def cyfrowe_dopelnienie(n):
    d = 0
    n_dup = n
    mnoznik = 1
    while n_dup > 0:
        #dla kazdej liczby która przechodzimy to bierzemy ją i odwracamy i dopisujemy ją do wyniku
        ostatnia = n_dup % 10

        dopelniajaca = 9 - ostatnia #jesli ostatnia to 6 to => 9-6 = 3

        d = d + dopelniajaca * mnoznik

        mnoznik *= 10
        n_dup = n_dup // 10 # skracamy o ostatnia cyfre

    return d

print(cyfrowe_dopelnienie(123456))

