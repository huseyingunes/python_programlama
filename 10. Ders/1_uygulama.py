"""
Kullanıcı arayüzü olacak
Arayüzden parite ve tarih aralıkları seçilecek
Paritenin mum tipi de seçilecek (1 dk, 5dk, 1saat vs.)
Grafik çizdirilecek
"""
from tkinter import *


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

cal=DateEntry(pencere, selectmode='day', textvariable=tarih_bas)
cal.grid(row=1, column=1, padx=15)

lbl33 = Label(pencere, text="Bitiş Tarihi")
lbl33.grid(column=0, row=2)

cal2=DateEntry(pencere, selectmode='day', textvariable=tarih_bit)
cal2.grid(row=2, column=1, padx=15)

def tiklandi():
    parite = variable.get()
    tarih_baslangic = tarih_bas.get()
    tarih_bitis = tarih_bit.get()

    pass

btn2 = Button(pencere, text="Grafik Çiz",
              bg="orange", fg="red",
              command=tiklandi
              )

btn2.grid(column=1, row=3)

variable = StringVar(pencere)
variable.set("BTCUSDT") # default value



# Seçenek kutusu oluşturma
secenekler = ["BTCUSDT", "ETHUSDT", "ADAUSDT"]
secenek_kutusu = OptionMenu(pencere,
                            variable,
                            *secenekler)

secenek_kutusu.grid(column=1, row=0)



# Seçenek kutusunu pencereye ekleme

# Pencereyi ekranda gösterme
pencere.mainloop()