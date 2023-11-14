"""
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdirin (veriler sqlite tan çekilecek).
"""
import sqlite3
import matplotlib.pyplot as plt

bag = sqlite3.connect("veri.vt")
cursor = bag.cursor()

parite = "ADAUSDT" #input("Pariteyi giriniz : ")
tarih_bas = "2022-01-01" #input("Başlangıç Tarihi (2022-01-01): ")
tarih_bit = "2022-01-02" #input("Bitiş Tarihi (2022-01-01): ")
deger = "open" #input("Hangi Değer (open, high, low, close): ")

cursor.execute('SELECT tarih_saat, '+deger+' from kripto WHERE '
               'parite="'+parite+'" AND '
               'tarih_saat BETWEEN "'+tarih_bas+'" AND "'+tarih_bit+'"')

rows = cursor.fetchall()
tarihler = []
degerler = []
for row in rows:
    tarihler.append(row[0])
    degerler.append(row[1])

import numpy as np
# Data for plotting

fig, ax = plt.subplots()
ax.plot(tarihler, degerler)

ax.set(xlabel='tarih saat', ylabel='value (USDT)',
       title='Başlık')
ax.grid()

fig.savefig("test.png")
plt.show()