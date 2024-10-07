'''
ADAUST dosyasını csv olarak okuyunuz.
Mayıs ayının açılış ortalamasını hesaplayınız...
'''

















import csv

with open('ADAUSDT_mum_1_yil_1_saatlik.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    ortalama, adet = 0, 0
    for i, row in enumerate(reader):
        if int(row["otime"].split(" ")[0].split("-")[1]) == 5:
            ortalama += float(row["open"])
            adet += 1
    ortalama = ortalama / adet
    print("Ortalama :", ortalama)
