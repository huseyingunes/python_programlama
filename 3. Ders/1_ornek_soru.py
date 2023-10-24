"""
kendisine gönderilen sayılardan sadece palindrom
olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.
örnek palindromlar:
    101
    6006
    75577557
"""

## ÇÖZÜM 24.10.2023
sayilar = [11, 20, 22, 10, 33]
topla = 0

palindrom_mu = lambda sayi: True if str(sayi) == str(sayi)[::-1] else False
cozum2023 = lambda sayi: sum([i if palindrom_mu(i) else -i for i in sayi])
print(cozum2023(sayilar))

## Daha iyi çözüm: (Recep Ürkün --> Chat GPT)
polinDRAM=lambda *dram: sum([i if str(i) == str(i)[::-1] else -i for i in dram])
print(polinDRAM(11, 20, 22, 10, 33))
##print(palindrom_mu(sayi))
quit()







def polinDRAM(*dram):
    toplam = 0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam


print(polinDRAM(10, 101, 55, 40, 9009))
