import math


def faktoriyel(sayi):
    f = 1
    for i in range(1, sayi + 1):
        f *= i
    return f


def yineleyici_faktoriyel(sayi):
    if sayi == 0:
        return 1
    else:
        return sayi * yineleyici_faktoriyel(sayi-1)



def karekok(sayi):
    return math.sqrt(sayi)
