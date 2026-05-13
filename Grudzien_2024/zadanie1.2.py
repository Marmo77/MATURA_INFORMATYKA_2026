
def J(n):
    #najpierw zamieniamy na binarna
    binarna = 0
    n_copy = n
    potega = 1
    while n_copy > 0:
        reszta = n_copy % 2
        binarna = binarna +reszta * potega
        potega = potega * 10
        n_copy = n_copy // 2
    index = 1
    while binarna > 0:
        ostatnia = binarna % 10
        if ostatnia == 1:
            print(index)
        index += 1
        binarna = binarna // 10
    #dla kazdego sprawdzamy czy jest 1
J(19)