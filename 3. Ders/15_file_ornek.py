'''
ADAUSDT parite dosyasını okuma modunda açınız.
Open, Close, High ve Low değerlerini okuyarak
ortalamalarını hesaplayıp ekrana yazdırınız.

Arka arkaya en çok kaç saat yükseldiğini ve düştüğünü
    yazdırınız.

'''

dosya = open("ADAUSDT_mum_1_yil_1_saatlik.csv", "r")
_open = _close = ysay = dsay = enf_yuk = enf_dus = 0
for i, satir in enumerate(dosya):
    if i == 0:
        continue
    satir = satir.split(",")
    _open = float(satir[1])
    _close = float(satir[4])

    if _open < _close:
        ysay += 1
        dsay = 0
        if enf_yuk < ysay:
            enf_yuk = ysay

    if _open > _close:
        dsay += 1
        ysay = 0
        if enf_dus < dsay:
            enf_dus = dsay

    if _open == _close:
        ysay = dsay = 0



print("En çok yükseldiği saat sayısı :", enf_yuk)
print("En çok düştüğü saat sayısı :", enf_dus)
dosya.close()

'''

5. saatten itibaren hareketli (5 saatlik) ortalamayı hesaplayınız
    ve bu değerleri tarih ile birlikte yazdırınız.
'''

dosya = open("ADAUSDT_mum_1_yil_1_saatlik.csv", "r")
_close = 0
degerler = []
for i, satir in enumerate(dosya):
    if i == 0:
        continue
    satir = satir.split(",")
    _close = float(satir[4])

    if 0 < i < 6:
        degerler.append(_close)
        continue

    ortalama = sum(degerler) / 5
    print(satir[0], ":", ortalama)
    degerler.remove(degerler[0])
    degerler.append(_close)

dosya.close()



'''
En yüksek artış ve düşüş gösterdiği günlerin
    tarih ve yüzdesel değerlerini yazdırınız.

'''

dosya = open("ADAUSDT_mum_1_yil_1_saatlik.csv", "r")
_close = _open = 0

for i, satir in enumerate(dosya):
    if i == 0:
        continue
    satir = satir.split(",")
    _close = float(satir[4])
    _open = float(satir[1])

dosya.close()
quit()












dosya = open("ADAUSDT_mum_1_yil_1_saatlik.csv", "r")
open_ortalama = 0
for i, satir in enumerate(dosya):
    if i == 0:
        continue
    satir = satir.split(",")
    open_ortalama += float(satir[1])
open_ortalama = open_ortalama / 8760
print("Open Ortalama :", open_ortalama)








import pandas as pd
veri = pd.read_csv("ADAUSDT_mum_1_yil_1_saatlik.csv")
df = pd.DataFrame(veri, columns=["otime", "open", "high", "low",
                            "close", "volume"])
print(df["open"].mean())
print(df["high"].mean())
print(df["low"].mean())
print(df["close"].mean())
