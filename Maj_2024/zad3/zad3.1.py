
n1 = 294762
n2 = 39101
def nieparzysty_skrot(liczba: int) -> int:
    m = 0
    c = 1
    while liczba > 0:
        ostatnia = liczba % 10 #ostatnia liczba
        
        # if ostatnia % 2 == 0: # jesli jest parzysta to nic nie robimy
            
            # print(f"parzysta: {ostatnia}")
            
        # else: #jesli jest nieparzysta to bierzemy wartosc nie parzysta i ustawiamy na pozycji swojej za pomoca c, i po dodaniu zwiekszamy c * 10 aby przesunac np. 947 - 7 * 1 = 7, 9 * 10 = 90 => 90+7 = 97
        if ostatnia % 2 != 0:
            # print(f"nieparzysta: {ostatnia}")
            m = m + c * ostatnia
            c = c * 10
        liczba = liczba // 10
        
    return m
    
print(nieparzysty_skrot(n1))
print(nieparzysty_skrot(n2))