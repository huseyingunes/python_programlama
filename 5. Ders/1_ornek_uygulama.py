"""
1 - veri isimli bir klasör oluşturun
2 - zip dsosyasını veri klasörüne çıkartın
3 - zip dosyası içindeki csv dosyalarının tüm içeriğini
    tek bir csv dosyasında birleştirin
    volume olmasın
4 - bu kayıtların tamamını sqlite veritabanına bir tablo
    oluşturarak yükleyin
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdirin (veriler sqlite tan çekilecek).
"""
import os
import csv
from zipfile import ZipFile
import sqlite3

## - 1
try:
    os.mkdir("veri")
except FileExistsError:
    print("Veri klasörü zaten var...")
    if os.path.exists("veri/tum_veri.csv"):
        os.remove("veri/tum_veri.csv")

## - 2
with ZipFile("pariteler_cikti_1hour_2022_2022.zip",
             'r') as zObject:
    zObject.extractall(path="veri")

## - 3
baslik = ["parite", "otime", "open", "high", "low", "close"]
tum_veriler = []
csv_dosyalari = os.listdir('veri')
for csv_dosyasi in csv_dosyalari:
    with open("veri\\"+csv_dosyasi, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tum_veriler.append(
                [csv_dosyasi.split("_")[0], row["otime"], row["open"],
                               row["high"], row["low"],
                                    row["close"]])
with open('veri/tum_veri.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(baslik)
    writer.writerows(tum_veriler)

bag = sqlite3.connect("veri.vt")
cursor = bag.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS kripto "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "parite TEXT, "
               "tarih_saat TEXT, "
               "open REAL, "
               "high REAL, "
               "low REAL, "
               "close REAL)") # Sorguyu çalıştırıyoruz.
bag.commit()

with open("veri\\tum_veri.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for i, row in enumerate(reader):
        cursor.execute("INSERT INTO kripto(id, parite, tarih_saat,"
                       "open, high, low,close) VALUES("
                       +str(i+2)+", '"
                       +row["parite"]+"', '"
                       +row['otime']+"', "
                       +row['open']+", "
                       +row['high']+", "
                       +row['low']+", "
                       +row['close']+")")


bag.commit()
bag.close()

''' 2022 cevabı
import os
import zipfile
import pandas as pd
import sqlite3
















bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()

if not os.path.exists("veri"):
    os.mkdir('veri')
    arsiv = zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')
    arsiv.extractall("veri/")

    tum_dosyalar = os.listdir("veri")
    pandas_csv_listesi = []
    for csv_dosya in tum_dosyalar:
        veri = pd.read_csv("veri/" + csv_dosya)
        del veri["volume"]
        veri["parite"] = csv_dosya.split("_")[0]
        pandas_csv_listesi.append(veri)

    birlesmis_csv_ler = pd.concat(pandas_csv_listesi)
    birlesmis_csv_ler.to_csv('hepsi.csv', index=False)
    cursor.execute("CREATE TABLE IF NOT EXISTS parite("
                   +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   +"parite TEXT, otime TEXT, open FLOAT, "
                   +"high FLOAT, low FLOAT, close FLOAT);")

    kayitlar = pd.read_csv("hepsi.csv")
    for row in kayitlar.itertuples():
        cursor.execute("INSERT INTO "
                       + "parite(parite,otime,open,high,low,close)"
                       + " VALUES("
                       + "'"+row.parite+"',"
                       + "'"+row.otime+"',"
                       + ""+str(row.open)+","
                       + ""+str(row.high)+","
                       + ""+str(row.low)+","
                       + ""+str(row.close)+")")
    bag.commit()


parite = input("Parite Giriniz :")
bas_tarih = input("Başlangıç Tarihi :")
bit_tarih = input("Bitiş Tarihi :")

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+bas_tarih+"' " \
        "AND '"+bit_tarih+"') " \
        "AND parite='"+parite+"'"
cursor.execute(sorgu)
sonuc = cursor.fetchall()
print(sonuc)

bag.close()
'''