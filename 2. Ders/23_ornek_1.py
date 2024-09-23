"""
Klavyeden kullanıcı istediği kadar sayı girebilecek.
Kullanıcının girdiği sayılardan eğer herhangi biri palindrom ise
O ana kadar girilen sayıların çarpımlarının yarısını bu sayı ile bölecek
Çıkan sonucu ekrana yazdıracak programı yazınız.
"""

sayilar = []
sayi = None
while True:
    sayi = input("Bir sayı giriniz :")
    if sayi == sayi[::-1]:
        break
    else:
        sayilar.append(sayi)

carpim = 1
for s in sayilar:
    carpim *= int(s)
carpim /= 2
carpim /= float(sayi)

print("Sonuc :", carpim)
