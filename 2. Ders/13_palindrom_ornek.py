"""
Kullanıcıdan bir sayı girmesini isteyiniz
Bu sayının palindrom olup olmadığını ekrana yazdırınız
for, enumerate ve else kullanınız
"""

sayi = input("Bir sayı giriniz: ")

for i, rakam in enumerate(sayi):
    if rakam != sayi[-(i+1)]:
        print("Değil")
        break
else:
    print("Bu sayı palindromdur")