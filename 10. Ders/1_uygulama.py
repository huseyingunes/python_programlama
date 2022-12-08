"""
Kullanıcı arayüzü olacak
Arayüzden parite ve tarih aralıkları seçilecek
Paritenin mum tipi de seçilecek (1 dk, 5dk, 1saat vs.)
Grafik çizdirilecek
"""
from tkinter import *
from cryptocmd import CmcScraper
import matplotlib.pyplot as plt
import numpy as np


# Pencere oluşturma
from tkcalendar import DateEntry

pencere = Tk()



pencere.geometry('500x400')

lbl = Label(pencere, text="Parite")
lbl.grid(column=0, row=0)

tarih_bas = StringVar()
tarih_bit = StringVar()

lbl22 = Label(pencere, text="Başlangıç Tarihi")
lbl22.grid(column=0, row=1)

cal=DateEntry(pencere, selectmode='day',
              textvariable=tarih_bas,
              date_pattern='dd-mm-yyyy')
cal.grid(row=1, column=1, padx=15)

lbl33 = Label(pencere, text="Bitiş Tarihi")
lbl33.grid(column=0, row=2)

cal2=DateEntry(pencere, selectmode='day',
               textvariable=tarih_bit,
               date_pattern='dd-mm-yyyy')
cal2.grid(row=2, column=1, padx=15)

def tiklandi():
    parite = variable.get()
    tarih_baslangic = tarih_bas.get()
    tarih_bitis = tarih_bit.get()
    scraper = CmcScraper(parite,
                         tarih_baslangic,
                         tarih_bitis)
    headers, data = scraper.get_data()
    tarih_verisi = []
    kapanis_degeri = []
    hareketli_ortalama = []
    for i, veri in enumerate(data):
        tarih_verisi.append(veri[0])
        kapanis_degeri.append(veri[4])
        if i > 4:
            ortalama = kapanis_degeri[i] + kapanis_degeri[i-1]
            ortalama += kapanis_degeri[i-2] + kapanis_degeri[i-3]
            ortalama += kapanis_degeri[i-4]
            hareketli_ortalama.append(ortalama / 5)
    hareketli_ortalama.append(0)
    hareketli_ortalama.append(0)
    hareketli_ortalama.append(0)
    hareketli_ortalama.append(0)
    tarih_verisi.reverse()
    kapanis_degeri.reverse()
    hareketli_ortalama.reverse()
    plt.plot(tarih_verisi, kapanis_degeri)
    plt.plot(hareketli_ortalama)
    plt.show()
    pass

btn2 = Button(pencere, text="Grafik Çiz",
              bg="orange", fg="red",
              command=tiklandi
              )

btn2.grid(column=1, row=3)

variable = StringVar(pencere)
variable.set("BTC") # default value



# Seçenek kutusu oluşturma
secenekler = ["BTC", "ETH", "ADA"]
secenek_kutusu = OptionMenu(pencere,
                            variable,
                            *secenekler)

secenek_kutusu.grid(column=1, row=0)



# Seçenek kutusunu pencereye ekleme

# Pencereyi ekranda gösterme
pencere.mainloop()