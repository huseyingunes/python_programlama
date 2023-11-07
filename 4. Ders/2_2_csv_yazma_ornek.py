'''
ADAUST dosyasını csv olarak okuyunuz
Tarih alanını ve ondalıklı birimleri Türkçe'ye uygun
    hale getiriniz. Ayraç olarak ta ; kullanınız.
'''

import csv
from datetime import datetime

baslik = ["otime", "open", "high", "low", "close", "volume"]

yeni_veriler = []
with open('ADAUSDT_mum_1_yil_1_saatlik.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tarih_saat = datetime.strptime(row["otime"], '%Y-%m-%d %H:%M:%S')
        yeni_tarih_saat = tarih_saat.strftime('%d.%m.%Y %H.%M.%S')
        y_open = row["open"].replace(".", ",")
        y_low = row["low"].replace(".", ",")
        y_high = row["high"].replace(".", ",")
        y_close = row["close"].replace(".", ",")
        y_volume = row["volume"].replace(".", ",")
        yeni_veriler.append([yeni_tarih_saat, y_open, y_high,
                             y_low, y_close, y_volume])

with open('ADAUSDT_TR_Bicimli.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(baslik)
    writer.writerows(yeni_veriler)
