'''
ADAUSDT parite dosyasını okuma modunda açınız.
Open, Close, High ve Low değerlerini okuyarak
ortalamalarını hesaplayıp ekrana yazdırınız.
'''

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
