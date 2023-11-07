import csv

baslik = ["sicaklik", "nem", "basinc"]
veri = [[30, 75.5, 10], [32.3, 50, 3]
        , [32, 50.5, 3.9]]

with open('sensor_veri.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)
