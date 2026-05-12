tablica_elem = [3,9,12,41,32,96,61]

def sortowanie_babelkowe(tablica):

    for i in range(len(tablica)):
        for j in range(0, len(tablica) - i - 1): # dla kazdego elementu wielkosc sprawdzania zmniejsza sie o i,
            # czyli po pierwszym przejsciu j juz nie jest np. 7-1=6, tylko 7-1-1 = 5
            