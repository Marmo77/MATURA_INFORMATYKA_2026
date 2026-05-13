
def J(n):
    binarna = bin(n)[2:]
    print(binarna)
    pozycje = []
    # binarna trzeba od tylu przejsc
    binarna = binarna[::-1]
    for i in range(len(binarna)):
        if binarna[i] == "1":
            pozycje.append(i+1)

    return f"Dla {n}: {pozycje}"

print(J(19))
print(J(6))
print(J(42))
print(J(75))


print(int("1001011",2))
