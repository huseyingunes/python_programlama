"""
1 - Klavyeden girilen 5 tane sayıyı bir listeye atarak
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca
    göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
    a = eval(input())
"""
dizi = []
a = eval(input())
dizi.append(a)
b= eval(input())
dizi.append(b)
c = eval(input())
dizi.append(c)
d = eval(input())
dizi.append(d)
e = eval(input())
dizi.append(e)

def sirala(n):
    return n**2 - 20

dizi.sort(key=sirala)

print(dizi)