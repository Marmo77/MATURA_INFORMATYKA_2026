tablica_elem = [3,12,41,32,9,96,61]

def sortowanie_babelkowe(tablica):

    for i in range(len(tablica)):
        for j in range(0, len(tablica) - i - 1): # dla kazdego elementu wielkosc sprawdzania zmniejsza sie o i,
            # czyli po pierwszym przejsciu j juz nie jest np. 7-1=6, tylko 7-1-1 = 5
            if tablica[j] > tablica[j + 1]: #jesli obecny element np. 41 jest wiekszy od 32, to zamieniamy ich miejscami,
                #czyli przepychamy najwiekszy element na koniec tablicy
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica

print(sortowanie_babelkowe(tablica_elem))