tablica_elem = [3,9,12,41,32,96,61]

#sortowanei przez wybieranie - porównujesz go ze wszystkimi następnymi jeśli znajdziesz mniejszy -> zamieniasz miejscami,
# dla kazdego elementu tablicy przechodzimy przez wszystkie nastepne,
# w tym przypadku dla 3 sprawdzamy - 9,12,41,... i porownujemy

def sortowanie(tablica):
    for i in range(0,len(tablica)): # zakres od początku do końca tablicy
        for j in range(i+1,len(tablica)): # dla każdego elementu tablicy przechodzimy przez następne jej elementy
            print(f"dla: {tablica[i]} sprawdzamy {tablica[j]}")
            #porównujemy czy następny element jest mniejszy od obecnego, jesli tak zamieniamy je miejscami
            #(szukamy najmniejszego elementu na miejsce pierwsze, drugie, itd.)
            if tablica[i] > tablica[j]:
                tablica[i], tablica[j] = tablica[j], tablica[i] # można je tak zamienić lub używając temp
    return tablica

nowa_tablica = sortowanie(tablica_elem)

print(nowa_tablica)
